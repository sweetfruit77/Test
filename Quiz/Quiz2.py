import re
custlist=[]
page=-1

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')  

    if choice=="I":
        print("고객 정보 입력")       
        customer={'name':'','sex':'','email':'','birthday':''}
        while True:
            for i in customer.keys():
                s = input()
                customer[i] = s
                if customer["sex"] != 'M' or 'F':
                    break                    
            custlist.append(customer)
           # for i in custlist:
  #              if custlist[i][2] ==  
  #         page += 1
        
    elif choice=="C":
        print("현재 고객 정보 조회")

    elif choice == 'P':
        print("이전 고객 정보 조회")
    elif choice == 'N':
        print("다음 고객 정보 조회")
    elif choice=='D':
        print("고객 정보 삭제")
    elif choice=="U": 
        print("고객 정보 수정")
    elif choice=="Q":
        print("프로그램 종료")
        break