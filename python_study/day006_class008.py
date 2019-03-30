class Person2(object):

    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    def get_name(self):
        print("get_name")
        return self._name
    
    def set_name(self,name):
        if name == "장나라":
            print("{}의 이름 사용은 불가능합니다.".format(name))
            return
        else:
            print('set_name:',name)
            self._name = name
    name = property(get_name,set_name)

if __name__ == "__main__":
    t = Person2("김기덕",30)
    t.set_name("장나라")
    print(t.get_name())
    