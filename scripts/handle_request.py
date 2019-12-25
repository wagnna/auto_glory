# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/7/6 10:44 
  @Auth : 可优
  @File : handle_request.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import json

import requests

from scripts.handle_log import do_logger


class HttpRequest:
    """
    处理请求
    """
    def __init__(self):
        self.one_session = requests.Session()

    def to_request(self, method, url, data=None, is_json=False, **kwargs):
        method = method.upper()
        if isinstance(data, str):
            try:
                data = json.loads(data)     # '{"mobilephone": "18911112345","pwd": "123456"}'
            except Exception as e:
                # print("异常为: {}".format(e))
                do_logger.error("将json转为Python中的数据类型时, 出现异常: {}".format(e))
                data = eval(data)     # '{1: 2, 'a': '珍珠'}'

        if method == 'GET':
            res = self.one_session.request(method=method, url=url, params=data, **kwargs)
        elif method == 'POST':
            if is_json:  # 如果is_json为True, 那么以json格式来传参数
                res = self.one_session.request(method=method, url=url, json=data, **kwargs)
            else:   # 否则, 以form表单来传参数
                res = self.one_session.request(method=method, url=url, data=data, **kwargs)
        else:
            res = None
            do_logger.error("不支持【{}】方法请求".format(method))

        return res

    def close(self):
        self.one_session.close()


if __name__ == '__main__':
    # 1. 构造请求的url
    login_url = "http://tj.lemonban.com/futureloan/mvc/api/member/login"
    recharge_url = "http://tj.lemonban.com/futureloan/mvc/api/member/recharge"

    # 2. 创建请求参数
    # login_params = {
    #     "mobilephone": "18911112345",
    #     "pwd": "123456"
    # }

    login_params = '{"mobilephone": "18911112345","pwd": "123456"}'
    recharge_params = {
        "mobilephone": "18911112345",
        "amount": "52000"
    }

    # 后端有可能会做反爬虫操作
    headers = {  # 构造一个请求头的字典信息
        "User-Agent": "Mozilla/5.0 Steven"
    }

    do_request = HttpRequest()
    # 先登录
    login_res = do_request.to_request('PoSt', url=login_url, data=login_params, headers=headers)

    # 然后再充值
    recharge_res = do_request.to_request('GEt', url=recharge_url, data=recharge_params, headers=headers)

    do_request.close()
    pass
