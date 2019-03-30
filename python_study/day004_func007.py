# 사용자 정의 함수(인자)
# 가변인자 *사용 입력인자를 여러개 넣을수 있게 해준다
# 변수명 앞에 * 한 개를 사용한다.
# 전달된 내용은 내부적으로 tuple로 전달된다.

def do_any_sum(*args):
    sum = 0
    for su in args:
        sum += su
    return sum

if __name__ == "__main__":
    print("합계 :",do_any_sum()) #입력인자 값을 넣지 않았을 때에도 실행이된다.
    print("합계 :",do_any_sum(1))
    print("합계 :",do_any_sum(1,2))
    print("합계 :",do_any_sum(1,2,3))
    print("합계 :",do_any_sum(1,4,5,6,7))