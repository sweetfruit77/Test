#sorted(iterable[,key][,reverse])
#정렬된 리스트를 반환
#key파라미터의 값은 하나의 인자를 받고,정렬 목적을 위한키를 리턴하는 함수가 되어야한다.

names = {'mary':10999,'sams':2111,"aimy":9778,"Tom":20245,"Michale":27115,"Bob":5887,"kelly":7855}

ret1 = sorted(names)
print(ret1)

def f1(x):
    return x[0]

def f2(x):
    return x[1]

ret2 = sorted(names.items(),key=f1)
ret3 = sorted(names,key=f1)
ret4 = sorted(names.items(),key=f2)
print(ret2)
print(ret3)
print(ret4)