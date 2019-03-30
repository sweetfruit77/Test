# call_by_value , call_by_reference
def call_by_value(num,mlist):
    num = num+1
    mlist.append("add1")

num = 10 #인트는 10이라는 값이 들어감
mlist = [1,2,3] #리스트는 객체의 주소값이 들어감

print(num,mlist)
call_by_value(num,mlist)
print(num , mlist)


# __name__  변수
