# 객체 지향
# 객체는 속성과 행위(메서드 ,기능)를 가지는 대상체이다.
# 속성은 객체가 가지는 값이며 행위는 객체가 수행할 수있는 기능을 말한다.
class Car:
    speed = 0
    def get_spped(self,up):
        self.spped = up
        return self.spped
    def accelate(self,start):
        self.speed += 10
        return self.speed 
    def Break(self,stop):
        self.spped=0
        return self.spped
a = Car()
print(a.get_spped(5))

b = Car()
print(b.get_spped(100))

c = Car()
print(c.accelate(0))

d = Car()
print(d.Break(100))