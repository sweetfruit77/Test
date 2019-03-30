#filter(func,iterable)
#iterable의 각 요소 중 func()의 반환 값이 참인 것만 묶어서 이터레이터로 반환
#filter는 for문이 자동탑재되어있다.
def isodd(num):
    if num % 2== 0:
        return False
    else:
        return True

def isalpha1(num):   
    if type(num) == type(""):
        return True
    else:
        return False

def isint(num):
    if type(num) == type(1):
        return True
    else:
        return False    

listdata = [1,2,3,4,5,6,7,8,9]
alpha = [1,"안녕",2,"무엇을 원해?"]
if __name__ == "__main__":
    print(list(filter(isodd,listdata)))
    print(list(filter(isalpha1,alpha)))
    print(list(filter(isint,alpha)))