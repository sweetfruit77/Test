import re 

regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.]$[a-zA-Z]{2.3}')
print(regex.match('1jdvk@naver.com'))
print(regex.match('kkd479@naver.com'))
print(regex.match('kkddd@naver.com'))
print(regex.match('knjro@naver.com'))
print(regex.match('jvdvk@naver.com'))