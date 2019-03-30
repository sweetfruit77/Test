class A:
    def pr(self):
        print('A')

# 오버라이딩, 재정의 되었다.
class SubA1(A):
    def pr(self):
        print("pr1")
    
class SubA2(A):
    #def pr(self):
    #   print("pr2")
    pass

s = SubA1()
s2 = SubA2()
s.pr()
s2.pr()
print("-"*20)