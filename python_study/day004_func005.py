#사용자 정의 함수(인자)
#기본인자(Default Argument)
#오버로딩 같은 이름으로 함수안에 입력인자 종류만 다르게 하는것 #파이썬 같은 경우는 대개로 입력받는 인자의갯수가 다르다

def circle_area(radius,pi=3.14):
    area = pi*(radius**2)
    return area

if __name__ =="__main__":
    print("반지름:",3,"면적:",circle_area(3,3.14))
    print("반지름:",3,"면적:",circle_area(3,5))
    print("반지름:",3,"면적:",circle_area(3))