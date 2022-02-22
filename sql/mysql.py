import pymysql
# #连接数据库  host地址     port端口    user账号     passWord密码   database你要操作的数据库名字
# con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password=123456,database='mytest')
#
# # 创建游标  执行sql   查询语句返回结果
# cur=con.cursor()
#
# #执行sql
# #查询student3表里的所有内容
# sql='select * from student3'
#
# #执行sql
# cur.execute(sql)
#
# #有结果 拿到结果   fetchone()显示一条数据   fetchall(指定显示几条数据)  fetchmany()显示表里所有内容
# result=cur.fetchmany()
#
# #查看返回结果
# print(result)
#-


#增加删除修改
#1.连接数据库
con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password=123456,database='mytest')
# print(con)
#2.创建游标 执行sql语句
cur=con.cursor()
#新增
sql="insert into student3(id,name,age,sex) values(10,'大铁锤'，30，'男')"

#修改
#sql="update student3 set name='铁柱' where id=10"

#删除
#sql="delete from student3 where id=10"

#执行sql
cur.execute(sql)
# 提交
cur.execute('commit')