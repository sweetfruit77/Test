def sum(a,b):
    return a+b

#자기 파일을 실행하면 호출되고 다른 파일에서는 실행되지 않는다.
if __name__ == "__main__":
    print('add a and b')
    print('a=10,b=20')
    print(sum(10,20))

