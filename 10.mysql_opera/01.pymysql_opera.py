# API: mysql这个程序所对外开放的接口, 我们程序员可以使用程序对这个接口进行调用,从而控制mysql的动作

import pymysql
import sys


mysql_connect = pymysql.connect(host='39.100.110.135', user='bavduer', password='(BavDu..0611)', port=3306, charset='utf8')
cursor = mysql_connect.cursor()

cursor.execute('create database if not exists cloud1903_python;')
cursor.execute('show databases;')
print(cursor.fetchall())

cursor.execute('use cloud1903_python;')
double3 = '''create table if not exists YBQ(
ID int not null primary key,
Name varchar(10) not null,
Sex varchar(5))
charset="utf8";'''
cursor.execute(double3)
cursor.execute('desc YBQ;')
print(cursor.fetchall())

cursor.execute('insert into YBQ values (2, "Meng", "M");')
cursor.execute('select * from YBQ;')
# print(cursor.fetchall())

userlist = []
for i in cursor.fetchall():
    for j in i:
        userlist.append(j)
print(userlist)

mysql_connect.commit()
mysql_connect.close()
sys.exit()

