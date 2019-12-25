
import os


# 获取项目根路径
# one_path = os.path.abspath(__file__)
# two_path = os.path.dirname(one_path)
# three_path = os.path.dirname(two_path)
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取测试数据datas所在目录的绝对路径
DATAS_DIR = os.path.join(BASE_DIR, 'datas')

# 获取测试用例文件所在绝对路径
TEST_DATAS_FILES_PATH = os.path.join(DATAS_DIR, 'cases.xlsx')

# 获取配置文件configs所在目录的路径
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
CONFIG_FILE_PATH = os.path.join(CONFIGS_DIR, 'testcase.conf')

# 日志文件所在目录路径
LOGS_DIR= os.path.join(BASE_DIR, 'logs')

# 测试报告所在目录路径
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

USER_ACCOUNTS_FILE_PATH = os.path.join(CONFIGS_DIR, "user_accounts.conf")

CASES_DIR = os.path.join(BASE_DIR, 'cases')
