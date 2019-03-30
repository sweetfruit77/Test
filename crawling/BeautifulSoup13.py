import urllib.request,time
from bs4 import BeautifulSoup


url='https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y'
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,'html.parser')
results = soup.select('.section_list_ranking li a')
for result in results:
    #print('제목:',result.attrs['title'])
    #print('링크:',result.attrs['href'])
    #print()
    url_content ='https://news.naver.com'+result.attrs['href']
    response_content = urllib.request.urlopen(url_content)
    soup_content=BeautifulSoup(response_content,'html.parser')
    content=soup_content.select_one('#articleBodyContents')
    #print(content.contents)
    #time.sleep(3)

    #가공작업
    output = ''
    for item in content.contents:
        #print(item)
        stripped = str(item).strip() #공백제거
        #print(stripped)
        if stripped =='': #빈문자열을 제거
            continue
        if stripped[0] not in['<','/']: #태그나 주석제거
            output =str(item).strip()
    print(output.replace('본문 내용TV플레이어',''))
    time.sleep(3)
    