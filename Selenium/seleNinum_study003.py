from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time , sys , urllib

driver = wd.Chrome(executable_path='./Selenium/data/chromedriver')

word = urllib.parse.urlencode({'query':'영화'})
#print(word)
url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&{}'.format(word)
#print(url)
driver.get(url)
time.sleep(3)
html =driver.page_source
soup = BeautifulSoup(html,'html.parser')
#titles = soup.select()