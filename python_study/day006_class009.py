class My(object):

    def __init__(self):
        self._name = "korea"
        print("My")
    
    def get_name(self):
        print("get_name:",self._name)
        return self._name

class SubMy(My):
    def __init__(self):
        super().__init__()
        print("SubMy")
    def sub_print(self):
        print("sub_print:", self.get_name())

if __name__ =="__main__":
    s = SubMy()
    print(s._name)
    print("메소드:",s.get_name())
    print("-"*20)
    s.sub_print()