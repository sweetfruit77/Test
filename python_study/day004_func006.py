# 사용자 정의 함수(인자)
# 키워드 사용 인자 전달
# 키워드 인자 사용 후 기본인자를 사용하면 인식이 되지 않는다.

def circle_area(radius,pi):
    result = pi *(radius**2)
    return result

if __name__ == "__main__":
    print("반지름 :",3,"면적 :", circle_area(3,pi=3.14))
    print("반지름 :",3,"면적 :", circle_area(radius=3,pi=3.14))
    print("반지름 :",3,"면적 :", circle_area(pi =3.14,radius=3))
    #print("반지름 :",3,"면적 :", circle_area(radius =3,3.14)) =>키워드 인자를 사용하면 뒤에도 무조건 키워드 인자를 사용해야한다.
    #print("반지름 :",3,"면적 :", circle_area(radius=3))