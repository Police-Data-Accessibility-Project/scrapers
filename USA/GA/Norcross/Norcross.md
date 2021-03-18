1. Go to https://www.norcrossga.net/DocumentCenter/
2. Departments>Police>Annual Reports
3. Open Inspect Element>Network
4. Click page 2, edit this POST 
   ![image](https://user-images.githubusercontent.com/40151222/111563943-48f3f800-876f-11eb-87bc-eb7e4f805d7e.png)
5. Network>Request>Request payload, change from default to `page=1&size=100`, leaving `id` and `getDocuments` the same. Increase size based on number of files ![image](https://user-images.githubusercontent.com/40151222/111564132-a1c39080-876f-11eb-9dd8-4c10b78f055c.png)
6. Network>Response>Response Payload    Copy all.
7. Paste into a document titled response.json, and run script

# Functions
`scrape_urls`: As the name implies, it extracts the urls from the website's JSON response and saves them in `urls.txt`
