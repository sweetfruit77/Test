# 사용자 정의 함수(인자)
#정의되지 않은 인자 전달
#정의되지 않는 인자 전달이 가능하며,이는 dict타입으로 전달됨
#일반인자 -> 가변인자 -> 정의되지 않는 인자 순으로 전달되어야 함

def circle_area(radius,*pi,**num):
    for item in pi:
        area = item *(radius**2) #pi는 여러개의값을 받고 있기 때문에 주소로 전달되어 계산이 안된다.
        print("반지름:",radius,"PI:",item,"면적:",area)

    for key in num:
        print(key,":",num[key])

if __name__ == "__main__":
    circle_area(3,3.314,3.1456,3.141592)
    print()
    circle_area(3,3.314,3.1456,3.141592,line_color="red",area_color="greed")