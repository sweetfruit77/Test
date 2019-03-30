#클래스 속성/인스턴스 속성
class STest:
    age = 10

s1 = STest() #인스턴스 속성
s2 = STest()
s2.gender = "남" # 인스턴스 속성 선언후 추가가 가능하다.(파이썬만 가능)
print(s2.gender)
#print(s1.gender)
s1.age = 30
s2.age = 50
print(s1.age)
print(s2.age)

print(STest.age) #클래스 속성