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
        customer['name'] = str(input("이름을 입력하세요 :"))
        
        while True: # 중복되지 않게 입력
            customer['sex'] = str(input("성별(M/m 또는 F/f)을 입력하세요 :"))
            customer['sex'] = customer['sex'].upper()
            if customer['sex'] in ('M' or 'F'):
                break
        while True:
            customer['email']=str(input("이메일을 입력하십시요"))
            check = 0
            for i in custlist:
                if i['email'] == customer['email']:
                    check=1
            if check ==0:
                break
            """
            regex = re.compile('@')
            golbang = regex.search(customer['email'])
            if golbang != None:
            else:
            """
        while True:
            customer['birthday'] = str(input("생년월일을 입력하십시요"))
            if len(customer['birthday']) == 4:
                    int(customer['birthday'])
                    break
        custlist.append(customer)
        page += 1
    elif choice=="C":
        print("현재 고객 정보 조회")
        if page >= 0:
            print("현재 페이지는 {} 쪽 입니다.".format(page + 1))
            print(custlist[page])
        else:
            print("입력된 정보가 없습니다.")

    elif choice == 'P':
        print("이전 고객 정보 조회")
        if page <= 0:
            print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다.')
            print(custlist[page])
        else:
            page -=1
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])
    elif choice == 'N':
        print("다음 고객 정보 조회")
        if page <= 0:
            print('고객님 정보는 페이지 이동이 불가합니다.')
            print(custlist[page])
        else:
            page+=1
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])
    elif choice=='D':
        print("고객 정보 삭제")
        choice1 = input("삭제하려는 고객 정보의 이메일을 입력하세요.")
        delok = 0
        for i in range(0,len(custlist)):
            while custlist[i]['email'] == choice1:
                print('{}고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
                del custlist[i]
                print(custlist)
                delok =1
                break

            if delok == 1:
                break

        if delok == 0:
            print('등록되지 않은 이메일입니다.')        
    elif choice=="U": 
        print("고객 정보 수정")
        
    elif choice=="Q":
        print("프로그램 종료")
        break

        #그것만 수정하도록 가능하게 만들어라
        #기능별로 함수로 다 분리시켜서 만들어라
        #클래스로 만들어서 돌아가겠끔해라