# 함수의스코프
g_val = 3 # 전역변수
def foo():
    l_val = 2 #지역변수
    g_val = 2 #지역변수
    print("in g_val:",g_val)
    print("in l_val:",l_val)


print("out g_val:",g_val)
#print("out l_val:",l_val) # 바깥쪽에서는 접근이 불가함

foo() #안에서는 불러다 쓰는데 아무 문제 없다.