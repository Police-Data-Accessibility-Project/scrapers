# Raw Record Representation Proposal

## BLUF

Upload fetched documents, having performed the minimal amount of processing. Define a manifest expressing the
association between those document URIs and basic metadata (ID, region and record type, timestamp of collection, etc.).
Sign that manifest and upload it. Now a logical record's components may be derived from the manifest and the now-stored
documents the manifest describes.

## Objective

Define a system for tracking the associations between the various crude scrapings that describe a record. How documents
are fetched and how software is deployed are both directly relevant to this space, but are out of scope for this
document.

## Background

Record collection like we're trying to do is a dumpster fire of inconsistency. In some cases the fields we want are in a
single document, but frequently the fields we require for a single logical record span multiple documents. Rather than
having every scraper developer wrestle with this complexity, present design discussions are leaning toward separate
source fetching and field extraction stages. This allows us to build a corpus of crude source material which may be more
easily refined offline, with greatly reduced risk of the extraction process tainting the original data.

Separately, there is a large concern surrounding tracking of data lineage to prevent (or at least reliably detect)
accidental or intentional tampering of data. Offline processing of the raw source data makes it possible to cheaply
iterate on extraction tooling and forward propagate the results, while also being able to compare against previous
extractions, without the need for querying a service with questionable availability and durability.

## Requirements

We need a way to store raw information pertaining to logical records. Given logical records can span documents, we also
need to store a representation (a manifest) of those relationships. Given records are capable of changing over time, we
need to be able to track distinct snapshots over time. Additionally, we need a service which will take this information
and persist it in a meaningful way. Analysis of this information is not in scope.

### Manifests

A manifest needs to be able to represent the raw materials associated with a record. The minimal identifiers for the
record itself are:
* a unique ID
* which region and record type the manifest represents (e.g., "USA/FL/Bay/Court")
* some sort of case identifier
* the timestamp of collection

A bunch of record-identifying metadata is cool, but we also need to be able to represent the documents that compose the
record. To that end, we'll require a list of document references. Each reference will contain:
* a content type (we can just use [MIME
types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) here)
* a digest of the content
* a URI for where that document's contents are durably stored in PDAP infrastructure
  * this isn't necessary if we adopt storage infrastructure that allows us to reliably derive this from the digest
* an optional comment expressing where this specific document came from

In order for us to trust our collected record results, we need to be able to verify that we trust the software which
performed the collection. This means being able to audit the code that created each manifest. To this end we also need
to include in our manifest:
* fetcher metadata
* what's our entrypoint for this scraper?
* what commit hash are we running from?
* a digital signature of the rest of the manifest
  * this is required to anchor our data lineage
  * key management is out of scope for this document (but the appendix touches on a half-baked approach)
* support for extension in the future (we can't be locked in to just these fields)

### Storage Endpoints
We need to be able to store the raw documents and manifests somewhere durable. This document doesn't have strong
opinions regarding how things are stored, but we need a specific API to ensure safe collection. Our collection API:
* must allow writing new documents and manifests
* must not allow for the fetching or altering of existing documents or manifests
* must enforce authentication and authorization for document submission
  * this lets us prevent unknown/untrusted entities from aiming a firehose of data at us and eating all of our money,
  but there's little risk of this threatening the trustworthiness of our records due to the lack of manifest
  * this document doesn't have a strong opinion here regarding how we authenticate, but the appendix has a strawman we
can use to start that conversation
* must not alter the manifest or its signature before committing to durable storage
  * without the signature, we can't detect tampering or associate the manifest with a fetcher
* should probably losslessly compress most things (we get 40% savings with gzip on the sample manifest below)
    
## Design Ideas
### Document Storage
First, let's talk document storage. Have record fetchers crawl however they want and upload documents to a document
storage endpoint. This should ideally be some kind of content-addressed blob storage service. We don't need a lot of
structure for this, as any relationship between documents will be encoded by the manifests -- the service just needs to
be able to store the raw documents for later lookup. Backing this storage API with a fairly flat filesystem is fine
here, we're rarely going to list files, only write and read. If we do need to list files, it'll be for some cleanup
operation and should not be on any request path.

A big benefit of content-addressed storage here is that we get deduping almost for free -- we may need to zero out
content that changes on every page load (e.g. "This page requested at HH:MM"), but that's more of an optimization than a
hard requrement. These savings would apply to both documents which remain unchanged between fetches and documents that
are shared between records.

The actual document collection service will take a file upload and respond with a simple payload denoting the URI that
may be used to access the file.

### Manifest Construction

Manifests need to be signed, so we'll just use [RFC 7519](https://tools.ietf.org/html/rfc7519) JWT blobs, encoding the
manifest's information in the JWT payload. As an example, the payload could resemble:

```json
{
  "version": 1,
  "uuid": "6e566397-6803-49ec-9280-62c00b368e3f",
  "record_type": "USA/FL/Bay/Court",
  "case_id": "20000001",
  "collected_at_ms": 1592618026000,
  "fetcher_id": "github.com/Police-Data-Accessibility-Project/Scrapers:USA/FL/Bay/Court/scraper/Scraper.py@1db20ce1e63768363d532d46a641722986f63524",
  "documents": [
    {
      "label": "some pdf we'll have to ocr",
      "content_type": "application/pdf",
      "digest": "...",
      "uri": "https://..."
    }, {
      "label": "party information",
      "content_type": "text/html",
      "digest": "...",
      "uri": "https://..."
    }
  ]
}	
```

Determining the PDAP-controlled URIs of the documents will require uploading them first, and then constructing the
manifest.

### Garbage Collection

Since this design requires documents to be uploaded before writing out a manifest, it's possible that we'll upload docs
and then fail (or neglect) to upload a manifest. This results in orphaned documents, which are just wasted storage. 
To mitigate this, we'll construct a GC batch job that runs on a schedule and removes documents that are orphaned and
have existed for longer than X time.

Finding orphaned documents has to be efficient. To this end, every write to the document storage service results in a
GC candidate entry. When a manifest is received referencing a given document, it is removed from the pool if it is
present. Periodically (daily? weekly?) the GC job will run to clean up all entries that have been there for a while
and remove them from the GC candidate pool.

## Caveats
This is somewhat complex and may be tricky to implement. A way to mitigate this is to invest in easy-to-use canonical
implementations in common languages with an API that makes misuse hard. For example, a Python API could resemble:

```python
with Record(record_type="USA/FL/Bay/Court", case_id="1337") as r:
  r.AddHtml("label1", html_file1)
  r.AddHtml("label2", html_file2)
  r.AddPdf("label3", pdf_file)
  r.commit()  # upload docs, make and upload manifest
```

## Appendix
### A half-baked proposal for JWT-based provenance verification
["Assume that a public key cryptosystem exists."](https://www.usenix.org/system/files/1401_08-12_mickens.pdf)
1. Fetcher generates a keypair (so no one has a copy), registers the public key with trusted infra
2. Trusted infra validates provenance of the requestor, records the information for auditing, wraps that provenance
information and the public key in a JWT and kicks it back
  * The JWT should have a short-ish lifespan (like a day?) in case it gets exported
  * We can also scope this JWT to the specific region and record type
  * It doesn't really matter how this JWT is signed (symmetric or asymmetric) and we can change this down the road if we
  want
3. Fetcher will make requests to the collection services using that JWT blob as a bearer token
4. Collection services will just verify the JWT for document uploads (after all, they're worthless without a manifest)
and verify all manifest signatures against the public key of the JWT blob
  * If we scope the auth JWT to the region and record type, we should verify the manifest matches that, as well
5. Downstream systems can verify manifest signatures against provenance verification audit logs (mentioned in 2) to
to ensure authenticity
  * This also enables retroactive disavowment of tokens (and all associated manifests) through a revocation list

What we're papering over here is how we verify provenance. I don't have a good answer here and whatever we end up with
will very likely strongly hinge on how we deploy our software (which is currently up in the air).

Let's say we have some infrastructure collect the provenance information and a nonce and wrap that in a short-lived JWT
signed with a symmetric key (say JWS's `HS256`). Then we plumb that JWT blob into the fetcher via an environment var or
a named pipe or something.

We could have that JWT provenance blob be one-time convertible for a longer-lived manifest-uploading JWT blob to
establish that relationship, but that doesn't change the fact that the provenance JWT blob is exportable.
