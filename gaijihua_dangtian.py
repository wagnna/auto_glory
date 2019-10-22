# -*- coding: utf-8 -*-

import random

import pymysql

from scripts.handle_config import do_config


class HandleMysql:
    """
    处理mysql
    """
    def __init__(self):
        self.conn = pymysql.connect(host='adcc-db-01.offline.hupu.com',
                                    user= 'adcc',
                                    password= 'Y6dn39Zy',
                                    db='ad_cc_hupu',
                                    port=3306,
                                    # charset=do_config.get_value('mysql', 'charset'),
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()


    def run(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args)
        self.conn.commit()

        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    # sql1 = 'SELECT * FROM member LIMIT 0, 10;'
    # sql2 = 'SELECT RegName, LeaveAmount FROM member WHERE MobilePhone = %s;'

    do_mysql = HandleMysql()
    # result = do_mysql.run("SELECT info FROM `cc_material_info` WHERE `id` = ress['ad']['id'] ", is_more=True)
    # sucai = 1142
    # sql_result = do_mysql.run("SELECT info FROM cc_material_detail WHERE `id` ="+str(sucai), is_more=True)
    import datetime

    # 获取今天的日期
    t_today = datetime.date.today()
    print(type(t_today))

    sql_r=do_mysql.run("UPDATE cc_plan SET ds= '%s',de= '%s' WHERE id=410076;" %(t_today,t_today),is_more=True)
    # print("UPDATE cc_plan SET ds= '%s',de= '%s' WHERE id=410076;" %(t_today,t_today))
    sql_a = do_mysql.run("UPDATE cc_schedule SET DATE='%s' WHERE pid=410076;"%(t_today), is_more=True)
    print("UPDATE cc_schedule SET DATE='%s' WHERE pid=410076;"%(t_today))
    sql_b = do_mysql.run("UPDATE cc_schedule_material SET DATE='%s' WHERE pid=410076;"%(t_today), is_more=True)
    print("UPDATE cc_schedule_material SET DATE='%s' WHERE pid=410076;"%(t_today))
    sql_c = do_mysql.run("UPDATE cc_plan SET ds= '%s',de= '%s' WHERE id=410024;"%(t_today,t_today) , is_more=True)
    print("UPDATE cc_plan SET ds=%s,de=%s WHERE id=410024;"%(t_today,t_today))
    sql_d = do_mysql.run("UPDATE cc_schedule SET DATE='%s' WHERE pid=410024;"%(t_today), is_more=True)
    print("UPDATE cc_schedule SET DATE='%s' WHERE pid=410024;"%(t_today))
    sql_e = do_mysql.run("UPDATE cc_schedule_material SET DATE='%s' WHERE pid=410024;"%(t_today), is_more=True)
    print("UPDATE cc_schedule_material SET DATE='%s' WHERE pid=410024;"%(t_today))
    # sql_result = do_mysql.run("UPDATE cc_plan SET ds='2019-10-22',de='2019-10-22' WHERE id=410076;", is_more=True)
    print("执行sql:修改计划时间为今天410024，410076")


