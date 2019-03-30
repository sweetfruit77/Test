class Student:
    def __init__(self,name="김기덕",age=1):
        self._name = name
        self._age =age
        print(name,"studnet객체가 생성되었습니다.")
        print(age,"나이가 설정되었습니다.")
    def showInfo(self):
        print(self._name,self._age)

s1 = Student()
s2 = Student("장나라")
s3 = Student(age=30)
s4 = Student("임꺽정",40)

s1.showInfo()

class human:
    name = ""
    age = 0
    height = 0
    hobby = ""
    gender = ""