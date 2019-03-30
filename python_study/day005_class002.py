#self
#객체 자신을 가리키는 특수한 변수
#다른 언어의 this키워드와 유사한개념을 가짐 (좀 달라)

class Sam_object(object):
    name = "korea"
    def get_name(self):
        return self.name
    
    def getInfo(self):
        self.get_name()

s1 = Sam_object()
s2 = Sam_object()
s3 = Sam_object()

s3.name="japan"
print(s1.name)
print(s2.name)
print(s3.name)
