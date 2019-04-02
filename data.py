import json
from urllib.request import urlopen, quote
import requests,csv
import pandas as pd #导入这些库后边都要用到
import pytz
from datetime import datetime

def participants_data(start=0,end=6):
    cities = pd.read_excel('data.xlsx', sheet_name='pcity')    
    return [ cities['addr'][i] for i in range(start,end) ]

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'hHaZWpPYRd8ce3NXPPOZIcglv60GXwCe'
    add = quote(address) #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp 

def get_timezone(address):
    # example : http://api.map.baidu.com/timezone/v1?coord_type=wgs84ll&location=-36.52,174.46&timestamp=1473130354&ak=你的ak
    # @sample address : trial_place
    # @return:  {'status': 0, 'timezone_id': 'Etc/GMT-1', 'dst_offset': 0, 'raw_offset': 3600}
    url = 'http://api.map.baidu.com/timezone/v1?coord_type=wgs84ll'
    add = address
    timestamp =  str(1473130354)
    ak = 'hHaZWpPYRd8ce3NXPPOZIcglv60GXwCe'
    uri = url + '&location=' + add + '&timestamp=' +  timestamp + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp 

def trans_utc(str):
    if '+' in str:
        str2 = str.split('+')[-1]
        x = str2.split(':')
        hour = int(x[0])
        minu = int(x[1])
        return hour*60+minu
    else:
        str2 = str.split('-')[-1]
        x = str2.split(':')
        hour = int(x[0])
        minu = int(x[1])
        return -(hour*60+minu)

"""
def tz_delta(addr1,addr2):
    print(get_timezone(addr1),get_timezone(addr2))
    tz1 = pytz.timezone(get_timezone(addr1)['timezone_id'])
    tz2 = pytz.timezone(get_timezone(addr2)['timezone_id'])
    str1 = str(datetime.now(tz1))
    str2 = str(datetime.now(tz2))
    delta = (trans_utc(str1) -  trans_utc(str2))/60
    return delta

addr1 = '31.2,121.5'
addr2 = '22.3,-121.9'
print(tz_delta(addr1,addr2))
"""
def tz_delta(addr1,addr2):
    delta = float(addr1.split(',')[1])-float(addr2.split(',')[1])
    #print(delta/15)
    return delta/15



