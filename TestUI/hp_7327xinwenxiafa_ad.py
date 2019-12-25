import requests
import json
import unittest
import requests
from scripts.handle_excel import *
import unittest
from urllib import parse
from urllib import parse
from urllib.request import urlopen
import urllib
from urllib.parse import urlparse,parse_qs
import json
# url = "https://test.mobileapi.hupu.com/3/7.3.27/cba/getNews"
#
# querystring = {"sign":"0e4024c96009ec5adccb061e5af79b78","news_first_navi":"CBA","pre_count":"0","advId":"C4BD5BA2-6682-425F-98BF-4A94D331F736","clientId":"30423397","nid":"0","first_navi_numbers":"9","preload":"0","direc":"next","num":"20","_ssid":"SFVQVS5XT1JL","night":"0","crt":"1571985309","time_zone":"America%2FNew_York","client":"B9F8C04E-8CB9-485A-B584-D99C4D80EC36","bddid":"67590695564"}
#
# response = requests.request("GET", url, params=querystring,verify=False)
#
# print(response.text)
# print(type(response.text))
# r_res=json.loads(response.text)
# print(r_res["result"]["recommend_data"])
import re
class Test_getother(unittest.TestCase):
    def test_dsp(self):
        file_name = r"D:\pro\hp_Apitestwn\Case\case_shouye.xlsx"
        one_excel = HandleExcel(file_name)
        values = one_excel.get_cases()
        print(values)
        print(type(values))
        for i in range(1,5):  #取出
            response = requests.request("GET", url=values[i]['url'],  params=values[i]['params'])
            # if ress['ad']['id']:
            ress=response.json()
            print(ress)
            # print(ress['ad_code'])

        # print(ress['share_data']['direct-response'])





if __name__ == '__main__':
    unittest.main()