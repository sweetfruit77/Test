from selenium import webdriver as wd
import sqlite3,urllib
from bs4 import BeautifulSoup
import time, sys

'''
webtoonlist = ['mon','tue','wed','thu','fri','sat','sun']
driver = wd.Chrome(executable_path='./Selenium/data/chromdriver')
for i in webtoonlist:    
    url = 'https://comic.naver.com/webtoon/weekday.{mon}'.format(mon=i)
    driver.get(url)
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    titles = soup.select()
'''
