import re

data ="""
park 800915-1049118
kim 700905-1059119
LEE 980603-2032072
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.match(data))

print(pat.sub("\g<1>-******",data))

p = re.compile('[a-z]+')
m = p.match("python")
s = p.match("")
print(s)
print(m)
