import MySQLdb

db = MySQLdb.connect(host='127.0.0.1' ,user ='root',\
    password ='qwer1324' ,database ='test' ,port=3306)

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : {} ".format(data))

db.close()