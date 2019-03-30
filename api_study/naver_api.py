import os
import sys
import urllib.request
client_id = "UGaGVj1srLm1eEGKlJ0M"
client_secret = "yIlAbeFsTU"
encText = urllib.parse.quote("봄나물")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode() #관련코드를 확인
if(rescode==200):
    response_body = response.read() # 응답을 읽어들임
    print(response_body.decode('utf-8'))
    #print(response_body[:100].decode('utf-8'))
else:
    print("Error Code:" + rescode)