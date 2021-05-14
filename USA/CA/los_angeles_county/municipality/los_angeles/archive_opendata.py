import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

save_url = [
    ["cfs/2019/", "https://data.lacity.org/resource/r4ka-x5je.csv"],
    ["crime_data/2010-19/", "https://data.lacity.org/resource/63jg-8b9z.csv"],
    ["arrests/2010-19/", "https://data.lacity.org/resource/yru6-6re4.csv"],
    ["cfs/2014/", "https://data.lacity.org/resource/mgue-vbsx.csv"],
    ["cfs/2020/", "https://data.lacity.org/resource/84iq-i2r6.csv"],
    ["drugs_poss/2010-2019/", "https://data.lacity.org/api/views/isxh-ztfe/rows.csv?accessType=DOWNLOAD"],
    ["cfs/2010/", "https://data.lacity.org/resource/iy4q-t9vr.csv"],
    ["cfs/2015/", "https://data.lacity.org/resource/tss8-455b.csv"],
    ["high_level_metrics/", "https://data.lacity.org/resource/t6kt-2yic.csv"],
    ["cfs/2013/", "https://data.lacity.org/resource/urhh-yf63.csv"],
    ["response_metrics/all_stations/", "https://data.lacity.org/resource/kszm-sdw4.csv"],
    ["cfs/2017/", "https://data.lacity.org/resource/ryvm-a59m.csv"],
    ["cfs/2011/", "https://data.lacity.org/resource/4tmc-7r6g.csv"],
    ["cfs/2016/", "https://data.lacity.org/resource/xwgr-xw5q.csv"],
    ["response_metrics/all_stations/2014/", "https://data.lacity.org/resource/y2p7-8ckf.csv"],
    ["response_metrics/citywide/2015/", "https://data.lacity.org/resource/jk5m-4dqg.csv"],
    ["response_metrics/citywide/2016/", "https://data.lacity.org/resource/8d58-axgy.csv"],
    ["response_metrics/citywide/unsure/", "https://data.lacity.org/resource/adam-59ei.csv"],
    ["response_metrics/all_stations/2015/", "https://data.lacity.org/resource/if3i-rtyg.csv"],
    ["cfs/2018/", "https://data.lacity.org/resource/nayp-w2tw.csv"],
    ["response_metrics/citywide/2017/", "https://data.lacity.org/resource/t69g-g3uk.csv"],
    ["response_metrics/all_stations/2013/", "https://data.lacity.org/resource/x88u-8etg.csv"],
    ["cfs/2012/", "https://data.lacity.org/resource/i7pm-cnmm.csv"],
    ["response_metrics/all_stations/2016/", "https://data.lacity.org/resource/ieyn-ppaw.csv"]




]

"save_folder" = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1, save_subfolder=True)
