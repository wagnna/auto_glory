# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/6/29 11:35 
  @Auth : 可优
  @File : handle_log_2.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import os
import logging
# 安装第三方模块concurrent-log-handler，解决多个进程处理同一个日志文件报错的问题
# 报错信息为：PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问
# pip install concurrent-log-handler
# from concurrent_log_handler import ConcurrentRotatingFileHandler

from scripts.handle_config import do_config
from scripts.constants import LOGS_DIR


class HandleLog:
    """

    """
    def __init__(self):
        self.case_logger = logging.getLogger(do_config.get_value("log", "logger_name"))
        self.case_logger.setLevel(do_config.get_value("log", "logger_level"))

        console_handle = logging.StreamHandler()
        # 输出到日志文件
        file_handle = logging.FileHandler(os.path.join(LOGS_DIR, do_config.get_value("log", "log_filename")),
                                          encoding="utf-8")

        # 4. 指定日志输出渠道的日志等级
        console_handle.setLevel(do_config.get_value("log", "console_level"))
        file_handle.setLevel(do_config.get_value("log", "file_level"))

        # 5. 定义日志显示的格式
        simple_formatter = logging.Formatter(do_config.get_value("log", "simple_formatter"))
        verbose_formatter = logging.Formatter(do_config.get_value("log", "verbose_formatter"))

        console_handle.setFormatter(simple_formatter)  # 终端显示简单结构的日志
        file_handle.setFormatter(verbose_formatter)  # 日志文件显示复杂结构的日志

        # 6. 对接, 将日志收集器与输出渠道进行对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        """

        :return:
        """
        return self.case_logger


do_logger = HandleLog().get_logger()


if __name__ == '__main__':
    case_logger = HandleLog().get_logger()
    case_logger.debug("这个是一个debug级别的日志信息")
    case_logger.info("这个是一个info级别的日志信息")
    case_logger.warning("这个是一个warning级别的日志信息")
    case_logger.error("这个是一个error级别的日志信息")
    case_logger.critical("这个是一个critical级别的日志信息")
