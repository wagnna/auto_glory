# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/7/13 10:03 
  @Auth : 可优
  @File : handle_context.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import re

from scripts.handle_mysql import HandleMysql
from scripts.handle_config import HandleConfig
from scripts.constants import USER_ACCOUNTS_FILE_PATH
# from cases.test_05_invest import loan_id


class Context:
    """
    实现参数化、接口依赖
    """
    not_existed_tel_pattern = r'\$\{not_existed_tel\}'  # 配置${not_existed_tel} 的正则表达式

    invest_user_tel_pattern = r'\$\{invest_user_tel\}'  # 配置${invest_user_tel} 的正则表达式
    invest_user_pwd_pattern = r'\$\{invest_user_pwd\}'  # 配置${invest_user_pwd} 的正则表达式
    invest_user_id_pattern = r'\$\{invest_user_id\}'  # 配置${invest_user_id} 的正则表达式
    #
    borrow_user_id_pattern = r'\$\{borrow_user_id\}'  # 配置${borrow_user_id} 的正则表达式
    not_existed_user_id_pattern = r'\$\{not_existed_user_id\}'  # 配置${not_existed_user_id} 的正则表达式
    #
    admin_user_tel_pattern = r'\$\{admin_user_tel\}'  # 配置${admin_user_tel} 的正则表达式
    admin_user_pwd_pattern = r'\$\{admin_user_pwd\}'  # 配置${admin_user_pwd} 的正则表达式
    #
    loan_id_pattern = r'\$\{loan_id\}'  # 配置${loan_id} 的正则表达式
    not_exitsed_loan_id_pattern = r'\$\{not_existed_loan_id\}'

    handle_config = HandleConfig(filename=USER_ACCOUNTS_FILE_PATH)

    @classmethod
    def not_existed_tel_replace(cls, data):
        """
        替换未注册的手机号
        :param data: 待替换的原始字符串
        :return:
        """
        if re.search(cls.not_existed_tel_pattern, data):
            handle_mysql = HandleMysql()
            not_existed_tel = handle_mysql.create_not_existed_mobile()  # 生成一个数据库中不存在的手机号
            data = re.sub(cls.not_existed_tel_pattern, not_existed_tel, data)
            handle_mysql.close()

        return data

    @classmethod
    def invest_user_tel_replace(cls, data):
        """
        替换已注册的手机号（使用已注册的投资人手机号）
        :param data:
        :return:
        """
        # if re.search(cls.invest_user_tel_pattern, data):
        invest_user_tel = cls.handle_config.get_value("invest_user", "mobilephone")  # 获取已经注册的投资人手机号
        data = re.sub(cls.invest_user_tel_pattern, invest_user_tel, data)
        return data

    @classmethod
    def invest_user_pwd_replace(cls, data):
        """
        替换已注册的密码（使用已注册的投资人账号的密码）
        :param data:
        :return:
        """
        # if re.search(cls.invest_user_pwd_pattern, data):
        invest_user_pwd = cls.handle_config.get_value("invest_user", "pwd")  # 获取已经注册的投资人用户密码
        data = re.sub(cls.invest_user_pwd_pattern, invest_user_pwd, data)
        return data

    @classmethod
    def invest_user_id_replace(cls, data):
        """
        替换已注册的投资人账号id
        :param data:
        :return:
        """
        # if re.search(cls.invest_user_id_pattern, data):
        invest_user_id = cls.handle_config.get_value("invest_user", "id")  # 获取已经注册的投资人用户id
        data = re.sub(cls.invest_user_id_pattern, invest_user_id, data)
        return data

    @classmethod
    def not_existed_user_id_replace(cls, data):
        """
        替换不存在的用户id
        :param data:
        :return:
        """
        if re.search(cls.not_existed_user_id_pattern, data):  # 替换一个不存在的用户id
            handle_mysql = HandleMysql()
            sql = 'SELECT MAX(Id) AS mid FROM member;'
            not_existed_user_id = str(handle_mysql.run(sql=sql)["mid"] + 1)  # 生成一个数据库中最大的用户id加1的数
            data = re.sub(cls.not_existed_user_id_pattern, not_existed_user_id, data)
            handle_mysql.close()
        return data

    @classmethod
    def admin_user_tel_pwd_replace(cls, data):
        """
        替换已注册的管理员手机号和密码
        :param data:
        :return:
        """
        # if re.search(cls.admin_user_tel_pattern, data):
        admin_user_mobile = cls.handle_config.get_value("admin_user", "mobilephone")  # 获取已经注册的管理员用户手机号
        data = re.sub(cls.admin_user_tel_pattern, admin_user_mobile, data)

        # if re.search(cls.admin_user_pwd_pattern, data):
        admin_user_pwd = cls.handle_config.get_value("admin_user", "pwd")  # 获取已经注册的管理员用户密码
        data = re.sub(cls.admin_user_pwd_pattern, admin_user_pwd, data)
        return data

    @classmethod
    def borrow_user_id_replace(cls, data):
        """
        替换已注册的借款人id
        :param data:
        :return:
        """
        # if re.search(cls.borrow_user_id_pattern, data):
        borrow_user_id = cls.handle_config.get_value("borrow_user", "id")  # 获取已经注册的借款人用户id
        data = re.sub(cls.borrow_user_id_pattern, borrow_user_id, data)
        return data

    @classmethod
    def register_parameterization(cls, data):
        data = cls.not_existed_tel_replace(data)
        # 第二个, 再来替换已注册的手机号
        data = cls.invest_user_tel_replace(data)
        return data

    @classmethod
    def loan_id_replace(cls, data):
        """
        替换存在和不存在的loan_id
        :param data:
        :return:
        """
        if re.search(cls.loan_id_pattern, data):  # 替换存在的loan_id
            loan_id = str(getattr(cls, "loan_id"))
            data = re.sub(cls.loan_id_pattern, loan_id, data)  # 获取loan_id

        if re.search(cls.not_exitsed_loan_id_pattern, data):  # 替换存在的loan_id
            handle_mysql = HandleMysql()
            sql = "SELECT MAX(Id) AS total_loan_id FROM loan LIMIT 0, 1;"
            not_existed_loan_id = str(handle_mysql.run(sql)["total_loan_id"] + 1)  # 生成一个数据库中最大的loan id加1的数
            data = re.sub(cls.not_exitsed_loan_id_pattern, not_existed_loan_id, data)
            handle_mysql.close()  # 关闭数据库连接

        return data

    @classmethod
    def login_parameterization(cls, data):
        """
        实现登录功能参数化
        :param data: 请求参数
        :return:返回参数化替换之后的结果
        """
        data = cls.invest_user_tel_replace(data)  # 替换已注册的投资人手机号
        data = cls.invest_user_pwd_replace(data)  # 再替换已注册的投资人用户密码
        return data

    @classmethod
    def recharge_parameterization(cls, data):
        """
        实现充值功能参数化
        :param data: 请求参数
        :return:返回参数化替换之后的结果
        """
        data = cls.invest_user_tel_replace(data)  # 替换已注册的投资人手机号
        data = cls.invest_user_pwd_replace(data)  # 替换已注册的投资人密码
        data = cls.not_existed_tel_replace(data)  # 替换未注册的手机号
        return data

    @classmethod
    def add_parameterization(cls, data):
        """
        实现加标功能参数化
        :param data: 请求参数
        :return:返回参数化替换之后的结果
        """
        data = cls.admin_user_tel_pwd_replace(data)  # 替换已注册的管理员手机号和密码
        data = cls.borrow_user_id_replace(data)  # 替换已注册的借款人用户id
        data = cls.not_existed_tel_replace(data)  # 替换一个不存在的用户id
        return data

    @classmethod
    def invest_parameterization(cls, data):

        data = cls.admin_user_tel_pwd_replace(data)  # 替换已注册的管理员手机号和密码
        data = cls.borrow_user_id_replace(data)  # 替换已注册的借款人用户id
        data = cls.loan_id_replace(data)  # 替换已存在和不存在的loan id
        data = cls.invest_user_tel_replace(data)  # 替换投资用户手机号
        data = cls.invest_user_id_replace(data)  # 替换投资用户id
        data = cls.invest_user_pwd_replace(data)  # 替换投资用户密码
        data = cls.not_existed_user_id_replace(data)  # 替换不存在的用户id
        return data


if __name__ == '__main__':
    data1 = '{"mobilephone": "${not_existed_tel}", "pwd":"123456"}'
    data2 = '{"mobilephone": "${not_existed_tel}", "pwd":"123456", "regname": "KeYou"}'
    data3 = '{"mobilephone": "1893434555", "pwd": "123456", "regname": "KeYou"}'
    print(Context.not_existed_tel_replace(data1))
    print(Context.not_existed_tel_replace(data2))
    print(Context.not_existed_tel_replace(data3))
