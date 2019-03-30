def circle_area(radius,pi):
    area = pi *(radius **2)
    circumference = 2 * pi *radius
    return area,circumference #여러개가 나올 상황이면 튜플로나온다.

if __name__ == "__main__":
    print("반지름:",3,"pi",3.14,"면적",circle_area(3,3.314))
    print("반지름:",3,"pi",3.1415,"면적",circle_area(3,3.31415))

    res1,res2 = circle_area(3,3.14)
    result = circle_area(3,3.14)
    print("반지름:",3,"면적과둘레:",result)
    print("반지름:",3,"면적:", res1,"둘레:",res2)