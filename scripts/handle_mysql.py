# -*- coding: utf-8 -*-

import random


from scripts.handle_config import do_config

import pymysql
class HandleMysql:
    """
    处理mysql
    """
    def __init__(self):
        self.conn = pymysql.connect(
                                # host='adcc-db-01.offline.hupu.com',

                                    # user= 'adcc',
                                    # password= 'Y6dn39Zy',
                                    # db='ad_cc_hupu',
                                    host='10.30.0.175',
                                    user= 'wangna',
                                    password= 'ELBl3cGhI2sQTKWZ',
                                    db='ad_adcc',
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
    t_today = datetime.datetime.now().strftime("%Y-%m-%d")
    print(type(t_today))
    print(t_today)

    # sql_r=do_mysql.run("UPDATE cc_plan SET ds= '%s',de= '%s' WHERE id=410076;" %(t_today,t_today),is_more=True)
    # result = do_mysql.run("SELECT material_id,date,stime,etime,show_times,sid  FROM `cc_schedule_material` WHERE  'date'='s'  and  adpid=  %s " % (t_today, 2130),is_more=True)
    # print("SELECT material_id,date,stime,etime,show_times,sid  FROM `cc_schedule_material` WHERE  'date'='%s' and `adpid`= %s"% (t_today, 2130))
    # print(result)
    result=do_mysql.run("select * from `cc_schedule_material` where `date` = '%s' and `adpid` = 4012 " % (t_today),is_more=True )
    # sq_sid = result[0]['sid']
    # sq_show_times =result[0]['show_times']
    sq_sid=result[0]['sid']
    print(result)
    print(result[0]['sid'])
    # print(result[0]['show_times'])
    sq_purpose=do_mysql.run("select * from `cc_schedule` where `id` = '%s'  " % (sq_sid),is_more=True )
    print(sq_purpose[0]['purpose'])

    # print(sq_sid)
    # print(sq_show_times)
    # if sq_sid ==1 :



