import urllib.parse
# 1解码  2 for i
# # urllib.parse.urlparse(url="")
# urllib.parse.parse_qsl(_.query)  # 使用urllib.parse.parse_qsl提取请求参数，返回列表
# Out[74]: [('aid', '44699780')]
#
# urllib.parse.parse_qs(_.query)   # 使用urllib.parse.parse_qs提取请求参数，返回字典
# Out[75]: {'aid': ['44699780']}
import urllib.parse
#urlsplit将url分为5个部分
url ="https://e-goblin-test.hupu.com/cm?fid=0&ad_type=todo&os=android&android_imei=866229037020359&brand_name=&first_navi_numbers=0&title=关注8位视频&type=第三方广告平台&client_id=23423412313523964&ios_idfa=&board_name=&union_name=ad-cc&show_type=6&first_navi=&ad_id=639&puid=32134716&request_number=1&nickname=石432145121&list_numbers=8&package_name=com.hupu.games&style=视频&entrances=社区推荐&android_id=7d9fabffdd43d53b&request_id=cddeb4f9544c4f44804c0fd43d8b3ff5"
url_change = urllib.parse.urlsplit(url)
print(url_change)
# query="fid=0&ad_type=todo&os=android&android_imei=866229037020359&brand_name=&first_navi_numbers=0&title=关注8位视频&type=第三方广告平台&client_id=23423412313523964&ios_idfa=&board_name=&union_name=ad-cc&show_type=6&first_navi=&ad_id=639&puid=32134716&request_number=1&nickname=石432145121&list_numbers=8&package_name=com.hupu.games&style=视频&entrances=社区推荐&android_id=7d9fabffdd43d53b&request_id=cddeb4f9544c4f44804c0fd43d8b3ff5', fragment=''"
# query="?fid=0&ad_type=todo&android_imei=866229037020359&first_navi_numbers=0&title=广告标题&type=第三方广告平台&client_id=23423412313523964&ios_idfa=&puid=32134716&request_number=1&nickname=石432145121&entrances=比赛&os=android&exposure_type=完全曝光&brand_name=&board_name=&union_name=ad-cc&show_type=12&first_navi=&ad_id=147&list_numbers=0&package_name=com.hupu.games&style=赛程套框&android_id=7d9fabffdd43d53b&request_id=9f8c020bad8647a4ad392d9afd731da1"
query="fid=0&ad_type=todo&os=android&android_imei=866229037020359&brand_name=&first_navi_numbers=3&title=titut1111&type=第三方广告平台&client_id=23423412313523964&ios_idfa=&board_name=&union_name=ad-cc&show_type=6&first_navi=NBA&ad_id=954&puid=32134716&request_number=1&nickname=石432145121&list_numbers=8&package_name=com.hupu.games&style=视频&entrances=新闻&android_id=7d9fabffdd43d53b&request_id=7a7cf0f7f94848eaa88f812cffa5a6f8"
query="list_numbers=8&entrances=新闻&first_navi_numbers=3&first_navi=NBA&board_name=&fid=0&topic_id=0&topic_name=&topic_category=&ad_id=521&request_id=edb14218ebe61785bb9004785af98fd1&android_id=7d9fabffdd43d53b&android_imei=866229037020359&ios_idfa=&type=内部使用&title=背景广告nba8位&style=背景广告&brand_name=hupu&union_name=ad-cc&package_name=&request_number=1&client_id=23423412313523964&ad_type=1000108&server_ip=10.64.56.169&puid=&nickname=&os=Android&os_version=8.0.0&app_version=7.3.23&wifi=1&network_type=wifi&link_type=__LINK_TYPE__&schema=__SCHEMA__"
lst_query = urllib.parse.parse_qsl(query)
list1=[]
for i in lst_query:
    list1.append(i[0])
print(list1)