# Setup

Within `configs.py`:
1. Set `url` to the url
1. set `department_code` to the first few letters of the url, and make them all capital. For example, the `department_code` of `https://hsupd.crimegraphics.com/2013/default.aspx` would be `HSUPD`.
1. `list_header`, This shouldn't need any changing, as it's just translating the columns into our `Fields`

# Module

The `crimegraphics_scraper` module requires two arguments, the `configs`, and the `save_dir`. Should you want performance stats, add `stats=True` as an argument.

# Info
The scripts should likely be run daily. They will only save the data if the hash (generated from the table) is different. Otherwise, it will simply exit. 
