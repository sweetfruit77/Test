import os
import sys
import urllib.request,sqlite3,json 


def movie_process(response_body):
    movieInformation = response_body.decode('utf-8')
    #print(movieInformation)
    
    data = json.loads(movieInformation)
    #print(data)
    dataKey = data['items'] 
    dataKey2 = []
    
    for i in dataKey:
        dataKey2.append(tuple(i.values()))
    #print(dataKey2)
    return dataKey2
    

client_id = "UGaGVj1srLm1eEGKlJ0M"
client_secret = "yIlAbeFsTU"
encText = urllib.parse.quote("영화")
url = "	https://openapi.naver.com/v1/search/movie.json?query=" + encText +"&display=10"  # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode() #관련코드를 확인
if(rescode==200):
    response_body = response.read() # 응답을 읽어들임
    #print(response_body.decode('utf-8'))
    #print(response_body[:100].decode('utf-8'))
 
    conn = sqlite3.connect('d:/pythonwork/api_study/example.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE if not exists movie
            (title text, link text , image text , subtitle text , pubDate text , director text ,actor text , userRating text)''')

    c.executemany('INSERT INTO movie VALUES(?,?,?,?,?,?,?,?)', movie_process(response_body))
    conn.commit()
else:
    print("Error Code:" + rescode)

