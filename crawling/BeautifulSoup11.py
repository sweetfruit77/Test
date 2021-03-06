import urllib ,sqlite3
from bs4 import BeautifulSoup

params = urllib.parse.urlencode({'page':1})
url='https://movie.naver.com/movie/point/af/list.nhn?&%s' %params
#print(url)

response = urllib.request.urlopen(url)
#print(response)
navigator = BeautifulSoup(response,'html.parser')
table = navigator.find('table',class_='list_netizen')
#print(table)

list_records=[]
for i,r in enumerate(table.find_all('tr')):
    for j,c in enumerate(r.find_all('td')):
        if j == 0:
            record={'번호':int(c.text.strip())}
        elif j==2:
            record.update({'평점':int(c.text.strip())})
        elif j==3:
            record.update({'영화':str(c.find('a',class_='movie').text.strip())})
            record.update({'140자 평':str(c.text).split('\n')[2]})
        elif j==4:
            record.update({'글쓴이':c.find('a',class_='author').text.strip()})
            record.update({'날짜':str(c.text).split('****')[1]})
        try:
            list_records.append(record)
        except:
            pass
#print(list_records)


conn = sqlite3.connect('d:/pythonwork/clolling/example.db')
c = conn.cursor()

c.execute('''create table if not exists movies
(Number real , grade real , movie text , Reviews text , author text , data text)''')

list_value = []

for i in list_records:
    list_value.append(tuple(i.values()))
print(list_value)
c.executemany('INSERT INTO movies VALUES(?,?,?,?,?,?)',list_value)
conn.commit()
