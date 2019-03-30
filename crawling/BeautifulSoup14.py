import sqlite3,urllib
from bs4 import BeautifulSoup

webtoonlist = ['mon','tue','wed','thu','fri','sat','sun']

for i in webtoonlist:    
    params = urllib.parse.urlencode({'week':i})
    url = 'https://comic.naver.com/webtoon/weekdayList.nhn?%s' %params
    #print(params)
    #print(url)
    response = urllib.request.urlopen(url)
    #print(response)

    navigator = BeautifulSoup(response,'html.parser')
    #print(navigator)
    table = navigator.find()