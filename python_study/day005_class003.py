class human:
    name = ""
    age = 0
    height = 0
    hobby = ""
    gender = ""

    def human_name(self,name):
        self.name = name
        return self.name
    def human_age(self,age):
        self.age = age
        return self.age
    def human_height(self,height):
        self.height = height
        return self.height
    def human_hobby(self,hobby):
        self.hobby = hobby
        return self.hobby
    def human_gender(self,gender):
        self.gender = gender
        return self.gender

Human01 = human()
Human_name = Human01.human_name("김기덕")
Human_age = Human01.human_age(30)
print("저의 이름은 :{} 입니다. 저의 나이는 {}입니다.".format(Human_name,Human_age))
 

    