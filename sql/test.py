from sql.mysqldb import MysqlDb

a=MysqlDb
b=a.select_query('select from * student3')
print(b)