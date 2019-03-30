# 속성 property

class Person1:

    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @name.setter
    def name(self,value):
        self._name = value    
    @age.setter
    def age(self,value):
        self._age = value

if __name__ == "__main__":
    p1 = Person1("김기덕",30)
    print(p1.name)
    p1.name = "배소진"
    p1.age = 25
    print(p1.name)
    print(p1.age)