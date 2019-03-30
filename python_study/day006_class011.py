#오버라이딩

class A:
    def func1(self):
        print("super")
class SubA1(A):
    def func1(self):
        print("SubA1")
class SubA2(A):
    def func1(self):
        print("SubA2")

def printA(a):
    a.func1()

a = A()
a1 = SubA1()
a2 = SubA2()
a.func1()
a1.func1()
a2.func1()
printA(a)
printA(a1)
printA(a2)