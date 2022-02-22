import configparser

import pymysql


class MysqlDb:
    def __init__(self,configpath,):
        #实力config
        config=configparser.ConfigParser()

        #读取文件数据
        config=configparser.ConfigParser()


        try:
            self.con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password=123456,database='mytest')
        except Exception as e:
            print('初始化连接失败'%e)
        self.cur=self.con.cursor()

    def select_query(self,sql):
        #执行sql
        try:
            self.cur.execute(sql)
            # 有结果 拿到结果   fetchone()显示一条数据   fetchmany(指定显示几条数据)  fetchall()显示表里所有内容
            result = self.cur.fetchmany(2)
            # print(result)
            return result
        except Exception as e:
            print('添加失败'%e)

    def idu_query(self,sql):
        try:
            #执行sql

            self.cur.execute(sql)
            self.cur.execute('commit')
        except Exception as e:
            print('增删改失败'%e)