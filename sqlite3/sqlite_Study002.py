import sqlite3
conn = sqlite3.connect('d:/pythonwork/sqlite3/example.db')
c = conn.cursor()

#Do this instead
t = ('RHAT',)
sql = 'SELECT * FROM stocks WHERE symbol=?'
c.execute(sql,t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28','BUY','IBM',1000,45.00),('2006-04-05','BUY','MSFT',1000,72.00)
,('2006-04-06','SELL','IBM',500,53.00),]

c.executemany('INSERT INTO stocks VALUES(?,?,?,?,?)',purchases)
conn.commit()

c.execute('select * from stocks ORDER BY price')
rows = c.fetchall()
for row in rows:
    print(row)

for row in c.execute('select * from stocks ORDER BY price'):
    print(row)

c.close()