 #예외처리

 #예외 처리 구문
def get(key,dataset):
    try:
        value = dataset[key]
    except IndexError:
        return None
    except KeyError:
        return None
    else:
        return value
print(get(3,(1,2,3)))
print(get('age',{'name':'홍길동','gender':True}))
        