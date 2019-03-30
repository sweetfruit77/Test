#함수의 인자와 반환값

def hello_message(repeat_count):
     for item in range(repeat_count):
         print("hello world")

if __name__=="__main__":
    a = hello_message(1)
    print(a)
    hello_message(2)