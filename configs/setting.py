#encoding = utf-8
import os
PROJ_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""请求问题规范"""
STANDARD = {0:"success",1001:"urlValueError",1002:"methodError",1003:"requestsData Type Error",\
            1004:"urlTypeError",1005:"methodValueError"}

METHOD = ["POST","GET","DELETE","PUT","HEAD"]

BODY_TYPE = ["FORM","JSON",None]

"""steps表位置"""
STEPS_FILENAME = os.path.join(PROJ_PATH,"Cases","step.xlsx")
STEPS_SHEETNAME = "steps"
"""cases表位置"""
CASES_FILENAME = os.path.join(PROJ_PATH,"Cases","cases.xlsx")
CASES_SHEETNAME = "cases"

"""smtp服务配置"""
MAIL_HOST = "smtp.qq.com"  # 设置服务器
MAIL_USER = "1300994936"  # 用户名
MAIL_PASS = ""  # 口令
MAIL_SENDER = "1300994936@qq.com" #发送邮箱
MAIL_RECEIVERS = ["zwq18616703217@163.com","mlwheiheihei@163.com"]
"""日志配置路径"""
CONF_PATH = os.path.join(PROJ_PATH,"Config","logger.conf")
TESTCASE_PATH=os.path.join(PROJ_PATH,"cases")
REPORT_PATH =os.path.join(PROJ_PATH,"reports")
if __name__ == "__main__":
    print(CONF_PATH)


