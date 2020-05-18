import pymysql
from inspect import *

conn = pymysql.Connect(
    host = 'localhost',
    user = 'ukhyun',
    passwd = 'dnr68425',
    db = 'test'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM MEMBER')
a = cursor.fetchall()
print(a)