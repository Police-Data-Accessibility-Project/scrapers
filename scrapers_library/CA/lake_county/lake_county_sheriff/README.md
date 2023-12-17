# Lake County Sheriff Scraper

## Source info

Records related to the Lake County Sheriff as part of California's SB 1421.

The records can be found online at [https://www.lakesheriff.com/969/Use-of-Force](https://www.lakesheriff.com/969/Use-of-Force)

## Content warning

Some of the videos and images contain graphic displays of police violence and bodily harm. Viewer discretion is advised.

## Storage and execution time

This scraper requires at least 14 GB of available disk space for all files and takes ~23 minutes to complete; dependant on disk and network speed.

## Content redaction

Video, audio, documents, and images may contain redacted data to protect the privacy of those involved.

## Objectively Reasonable

>The legal standard used to determine the lawfulness and appropriateness of a use of force is the Fourth Amendment to the United States Constitution. See Graham versus Connor, 490 U.S. 386 (1989). Graham states in part, The reasonableness of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight. The calculus of reasonableness must embody allowance for the fact that police officers are often forced to make split-second judgments - in circumstances that are tense, uncertain, and rapidly evolving - about the amount of force that is necessary in a particular situation. The test of reasonableness is not capable of precise definition or mechanical application. The force must be reasonable under the circumstances known to the officer at the time the force was used. Therefore, the Sheriff's Office examines all uses of force from an objective standard, rather than a subjective standard.

## Sample response

Sample response is ommitted due to many of the files being large in size.

The final folder structure is as follows:

- `./data/Case 21438/`
- `./data/Case 23408/`
- `./data/Case 01070402/`
- `./data/Case 08020293/`
- `./data/Case 10080048/`
- `./data/Case 14010032/`
- `./data/Case 14110123/`
- `./data/Case 15020285/`
- `./data/Case 17030017/`
- `./data/Case 18020066/`
- `./data/Case 19070164/`
- `./data/Case 19120322/`
- `./data/Case 20020144/`
- `./data/Case 20120287/`
- `./data/Case 21050095/`
- `./data/Case 21090240/`
- `./data/Case 22010120/`
- `./data/Case 23110157/`
- `./data/IA 2018-0023/`

## Requirements

- `Python 3`
- `requests`
- `tqdm`
- `m3u8`
- `pytube`
- `BeautifulSoup4`
- `inputtimeout`
- `from_root`
