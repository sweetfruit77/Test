from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time , sys , urllib

driver = wd.Chrome('./Selenium/data/chromedriver')

driver.get('https://www.google.co.kr/?hl=ko')

selectLan = '구글지도'
driver.execute_script("document.getElementsByName('q')[0].value=\'"+selectLan+"\'")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').click()