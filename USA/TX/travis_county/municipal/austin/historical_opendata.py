import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://data.austintexas.gov/resource/spbg-9v94.csv",
    "https://data.austintexas.gov/resource/8iue-zpf6.csv",
    "https://data.austintexas.gov/resource/sc6h-qr9f.csv",
    "https://data.austintexas.gov/resource/iydp-s2cf.csv",
    "https://data.austintexas.gov/resource/79qh-wdpx.csv",
    "https://data.austintexas.gov/resource/cpxf-2jga.csv",
    "https://data.austintexas.gov/resource/idj2-d9th.csv",
    "https://data.austintexas.gov/resource/h8jq-pcz3.csv",
    "https://data.austintexas.gov/resource/7guv-wkre.csv",
    "https://data.austintexas.gov/resource/eqwy-k8kh.csv",
    "https://data.austintexas.gov/resource/mipf-8at9.csv",
    "https://data.austintexas.gov/resource/xfke-9bsj.csv",
    "https://data.austintexas.gov/resource/3t4q-mqs5.csv",
    "https://data.austintexas.gov/resource/idj2-d9th.csv",
    "https://data.austintexas.gov/resource/mw6q-k5gy.csv",
    "https://data.austintexas.gov/resource/x4p3-hj3y.csv",
    "https://data.austintexas.gov/resource/mipf-8at9.csv",
    "https://data.austintexas.gov/resource/pgvh-cpyq.csv",
    "https://data.austintexas.gov/resource/uzqv-9uza.csv",
    "https://data.austintexas.gov/resource/u2k2-n8ez.csv",
    "https://data.austintexas.gov/resource/q5ym-htjz.csv",
    "https://data.austintexas.gov/resource/mi2a-twn5.csv",
    "https://data.austintexas.gov/resource/bmz9-cdnt.csv",
    "https://data.austintexas.gov/resource/5evd-3tba.csv",
    "https://data.austintexas.gov/resource/5w6q-adh8.csv",
    "https://data.austintexas.gov/resource/urfd-wng9.csv",
    "https://data.austintexas.gov/resource/jipa-v8m5.csv",
    "https://data.austintexas.gov/resource/fk9e-2udt.csv",
    "https://data.austintexas.gov/resource/bx9w-y5sd.csv",
]

# Change to what you need (remove what you don't)
save_table = [
    "annual_crime/2015/",
    "annual_crime/2016/",
    "racial_profiling/2015/citations/",
    "r2r/2015/",
    "hate_crimes/2017/",
    "arrests/guide/",
    "hate_crimes/2018/",
    "r2r/2016/",
    "racial_profiling/2017/citations/",
    "officer_involved_shooting/guide/",
    "racial_profiling/2018/guide/",
    "arrests/2018/",
    "annual_crime/2017/",
    "hate_crimes/2018/",
    "racial_profiling/2014/citations/",
    "racial_profiling/2017/arrests/",
    "racial_profiling/2018/guide/",
    "annual_crime/2018/",
    "officer_involved_shooting/2008-2017/",
    "officer_involved_shooting/2008-2017/subjects/",
    "r2r/2010/",
    "hate_crimes/2020/",
    "arrests/2016/",
    "r2r/2017/",
    "r2r/2017/subjects/",
    "citations/2016/",
    "r2r/2011/",
    "racial_profiling/2014/arrests/",
    "r2r/2012/"

]
save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
