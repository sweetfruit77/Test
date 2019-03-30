# 람다(Lamda)함수 == 익명함수
pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]

#def shortKey(pair):
    #return pair[1]

#pairs.sort(key=shortKey)
pairs.sort(key=lambda pair:pair[0])
print(pairs)