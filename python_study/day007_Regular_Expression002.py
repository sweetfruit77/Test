import re

p = re.compile("ca*t")
print(p.match("cat"))
print(p.match("ct"))
print(p.match("caaaaat"))

print(p.match("ca*t"))


g = re.compile('ca+t')
print(g.match("ct"))
print(g.match("cat"))
print(g.match("caaaaaat"))


print(g.match("caaabt"))
print(g.match("ca+t"))


f = re.compile('ca{2}t')

print(f.match("cat"))
print(f.match("caat"))

#0,1 
E = re.compile('ab?c')
print(E.match("ac"))
print(E.match("abc"))
print(E.match("abbc"))

#반복(^,$)
F = re.compile('^abc')
print(F.search('abcefc'))

fin = re.compile('^abc')
print(fin.findall("abcd"))