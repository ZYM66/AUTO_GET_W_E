import numpy as np
import pandas as pd
import json
import requests
import time




data = pd.read_csv('医院.csv', encoding='gbk')
col_1 = data['机构名称']
data_1 = np.array(col_1)
ak = 'ws8sWxM2eWTnH2TujUCBDd7mYvvvsi7c'
count = 0
dic = {}
for info in data_1:
    baseurl = 'https://api.map.baidu.com/place/v2/suggestion?query={}&region=北京&city_limit=true&output=json&ak={}'.format(
        info, ak)
    response = requests.get(baseurl)
    info1 = response.json()
    try:
        dic[info] = {
            "医院名称": info,
            "纬度": info1['result'][0]['location']['lat'],
            "经度": info1['result'][0]['location']['lng']
        }
        count = count + 1
        print("已经获取:" + info)
        print("当前为第" + str(count) + "个")
        time.sleep(0.5)
    except:
        print(info1['message'])

with open('new经纬度JSON.json', 'w', encoding="utf-8") as f:
    json.dump(dic, f, ensure_ascii=False)
    print("已生成json文件...")
