#Lambda  인자들 표현식

#아주 작으며 이름이없는 함수
#문법적으로는 하나의 표현식 만 사용되어야 함

def hap(x,y):
    return x+y

print(hap(10,20))
print((lambda x,y:x+y)(10,20))
