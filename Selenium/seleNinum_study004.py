from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time , sys , urllib

driver = wd.Chrome('./Selenium/data/chromedriver')
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')

'''
driver.find_element_by_name('id').send_keys('kkd479')
driver.find_element_by_name('pw').send_keys('비밀번호')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

'''

id = 'kkd479'
pw = 'Tjdfud12@@'

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(1)
#element창 로그인버튼 소스 선택된 상태에서 마우스 오른쪽 버튼 클릭 copy
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login_maintain"]/span[1]/a').click()

#네이버 쪽지 구하기
driver.get('https://note.naver.com/')
html = driver.page_source
soup = BeautifulSoup(html , 'html.parser')
notices = soup.select('span.from > a')
for i in notices:
    print(i.text)
