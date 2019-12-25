# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/7/16 19:38
  @Auth : 可优
  @File : handle_user.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
from scripts.handle_mysql import HandleMysql
from scripts.handle_request import HttpRequest
from scripts.handle_config import do_config
from scripts.constants import USER_ACCOUNTS_FILE_PATH


def create_new_user(regname, pwd="123456"):
    """
    创建一个用户
    :param regname:
    :param pwd:
    :return:
    """
    handle_mysql = HandleMysql()
    send_request = HttpRequest()
    url = do_config.get_value("api", "prefix_url") + "/member/register"
    sql = "SELECT Id FROM member WHERE MobilePhone=%s;"
    while True:
        mobilephone = handle_mysql.create_not_existed_mobile()
        data = {"mobilephone": mobilephone, "pwd": pwd, "regname": regname}
        send_request.to_request(method="post",
                                url=url,
                                data=data)
        result = handle_mysql.run(sql=sql, args=(mobilephone,))
        if result:
            user_id = result["Id"]
            break

    user_dict = {
        regname: {
            "Id": user_id,
            "regname": regname,
            "mobilephone": mobilephone,
            "pwd": pwd
        }
    }
    handle_mysql.close()
    send_request.close()

    return user_dict


def generate_users_config():
    """
    生成三个用户信息
    :return:
    """
    users_datas_dict = {}
    users_datas_dict.update(create_new_user("admin_user"))
    users_datas_dict.update(create_new_user("invest_user"))
    users_datas_dict.update(create_new_user("borrow_user"))
    do_config.write_config(users_datas_dict, USER_ACCOUNTS_FILE_PATH)


if __name__ == '__main__':
    # print(generate_users_config())
    # do_config.write_config(generate_users_config(), "user_accounts.conf")
    generate_users_config()
