# 예외 처리 구문
# 오류 종류를 전달 받아서 처리하기

try:
    a = [1,2]
    print(a[3])
    4/0
    print("end")
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a=[1,2]
    print(a[3])
    4/0
    print("end")
except (ZeroDivisionError,IndexError) as e:
    print(e)