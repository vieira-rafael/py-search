# -*- coding: utf-8 -*-"""Created on Sat Aug 01 17:28:29 2015@author: lenovo"""from datetime import datetimeimport pandas as pd""""""_START_ = '1994-01-01';_MIDDLE_ = '2015-11-27';_TODAY_ = datetime.now().strftime('%Y-%m-%d');_RATE_FREE_ = 0.05
_start_range = pd.date_range(start=_START_,periods=7)_end_range = pd.date_range(end=_MIDDLE_,periods=7)

""""""_PATH_CODE_ = 'd:/data/code.csv';_ENGINE_ = 'postgresql://postgres:root@localhost:5432/tushare'
#pgrestest_DATABASE_ = 'tushare'_USER_ = 'postgres'_PASSWORD_ = 'root'_HOST_ = '127.0.0.1'
_LOG_FILENAME_ = 'logging.conf' #_LOG_CONTENT_NAME_ = 'pg_log' #
__SQL1_ = '''CREATE TABLE ts_his(        date INTEGER,        sv_productname VARCHAR(32)        );'''