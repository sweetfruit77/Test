#함수를 반환하는 함수
def make_incrementor(n):
    print("n :",n)
    return lambda x: x+n
f = make_incrementor(42)

if __name__ == "__main__":
    print(f)
    print(f(0))
    print(f(1))

    print(make_incrementor(65)(1))