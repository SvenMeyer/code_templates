import os
import time
import gzip
import json
import pandas as pd

HOME_DIR = "/media/sf_SHARE"
if not os.path.isdir(HOME_DIR):
    HOME_DIR = os.path.expanduser("~")
WORK_DIR = os.path.join(HOME_DIR, "ML_DATA/GFK/AddThis/")
input_dir = os.path.join(WORK_DIR , 'data')
print("input_dir =", input_dir)
output_dir = os.path.join(WORK_DIR , 'data_panel')
print("output_dir =", output_dir)

cookie_df  = pd.read_csv(os.path.join(WORK_DIR,'addthis_cookies_2017-04-12.csv'))
cookie_set = set(cookie_df['addthis_uid'])

datafile = "pixelview-turbo-no-porn-de.20170320-0000.0000.log.gz"

i=0
n=0
with gzip.open(os.path.join(input_dir, datafile), 'r') as f:
#   lines = f.readlines()
    lines = [x.decode('utf8').strip() for x in f.readlines()]
    print(lines[0])
    print(lines[0].split('\t'))
    for line in lines[1:]:
        i += 1
        cookie = line.split('\t')[1]
        if cookie in cookie_set:
            n += 1
            print(line)
'''
        d = json.loads(line)
        # print(i, d['hhid'],d['uid'],d['cookieid'],d['featurekey'],d['featurevalue'])
        # make each line a real name-value dictionary
        dict_nv = {'hhid':d['hhid'] , 'uid':d['uid'] , 'cookieid':d['cookieid'] , d['featurekey']:d['featurevalue']}
        # df_nv = pd.DataFrame.from_dict(dict_nv)
        df_nv = pd.DataFrame(columns=['hhid', 'uid', 'cookieid'])  # , index=['hhid','uid','cookieid'])
        df_nv = df_nv.set_index(['hhid', 'uid', 'cookieid'])
        df_nv = df_nv.append(dict_nv, ignore_index = True, verify_integrity = False)
        # print(i, dict_nv)
        print(df)
        print(df_nv)
        print("-------")
        df=pd.concat([df,df_nv], ignore_index=False, verify_integrity=False)

print(df.info())
print(df)
'''
print(i, "lines processed")
print(n, "panel cookies found")