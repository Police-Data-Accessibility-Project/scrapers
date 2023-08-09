# Instructions

Go to their [administration page](https://www.carrolltonpd.com/divisions/administration/), on the right side, "crime reports"


On the cityprotect website, select "Download crimemap data" and click go ![image](https://user-images.githubusercontent.com/40151222/112383242-40497780-8cc3-11eb-9445-6cf695f2449a.png)


Choose a report (doesn't matter)


![image](https://user-images.githubusercontent.com/40151222/112383296-548d7480-8cc3-11eb-8f44-6aef21de5daf.png)


With the networking tab open, click "download" (after accepting the data policy and terms). After clicking download, close the download prompt and look in the networking tab. The request will look something like this


![image](https://user-images.githubusercontent.com/40151222/112383534-99191000-8cc3-11eb-873a-c1ee34401947.png)


An example request url is: https://cereplicatorprodcomm.blob.core.windows.net/mainblob/1423-10.2020-01.2021.csv?st=2021-03-24T21%3A08%3A22Z&se=2021-03-24T21%3A13%3A22Z&sp=r&sv=2018-03-28&sr=b&sig=%2FXuaM%2FHtueclub8li3oWGUTHCxcThpRVH62PlkTxaCk%3D


Strip the tracker, located after the `.csv`, leaving just
https://cereplicatorprodcomm.blob.core.windows.net/mainblob/1423-10.2020-01.2021.csv


The file name format is `police_code`-`start_month`.`start_year`-`end_month`.`end_year`, so
`police_code = 1423`


Scroll down to the bottom of the report list, and set [`start_year`](https://github.com/CaptainStabs/Scrapers/blob/master/scrapers/GA/Carrollton/carrollton_scraper.py#L14) to the lowest year of data available.


If the data is not current, comment out [line 200](https://github.com/CaptainStabs/Scrapers/blob/master/scrapers/GA/Carrollton/carrollton_scraper.py#L20), and close the block comment on [line 24](https://github.com/CaptainStabs/Scrapers/blob/master/scrapers/GA/Carrollton/carrollton_scraper.py#L24)
