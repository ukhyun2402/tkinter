import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'ukhyun',
    passwd = 'dnr68425',
    database = 'test'
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM MEMBER")

