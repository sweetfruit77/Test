import sqlite3

conn = sqlite3.connect('d:/pythonwork/sqlite3/example.db')
#conn = sqlite3.connect('./sqlite3/example.db')
c = conn.cursor()

#Create table

c.execute('''CREATE TABLE if not exists stocks
            (date text, trans text , symbol text, qty real, price real)''')

#Insert a row of data
c.execute("INSERT INTO stocks VALUES('2006-01-05','BUY','RHAT',100,35.14)")

#Sava(commit) the changes
conn.commit()

#we can also close the connection if we are done with it.

conn.close()