import re
custlist =[]
page = -1
line = "="*40
NumberCheck = re.compile('[0-9]+')
TextCheck = re.compile('[a-z]+')
def exe(choice):
    if choice == "I":
        insertData()
    elif choice == "C":
        curSearch()
    elif choice == "P":
        preSearch()
    elif choice == "N":
        nextSearch()
    elif choice == "U":
        updateData()
    elif choice == "D":
        deleteData()
    elif choice == "Q":
        quit() 
def insertData():
    customer = {"name":"","sex":"","email":"","birthday":""}
    print("고객 정보 입력")
    while True:
        print("이름을 등록해주세요")
        cRegistration = input()
        if cRegistration == "" or NumberCheck.match(cRegistration):
            print("이름을 제대로 입력해주세요.")
            cRegistration
        else:
            customer["name"] = cRegistration
            print("이름이 등록 완료 됬어요! 멋진 이름이에요 다음으로 넘어가요")
            #custlist.append(customer)
            #print(custlist)
            break
    while True:
        print(line)
        print("당신의 성별을 등록해주세요")
        cRegistration = input().upper()
        customer["sex"] = cRegistration
        # in으로 리스트 안에서 특정 요소가 존재하는지 확인합니다.
        if customer["sex"] == "M" or customer["sex"] == "F": #customer['sex'] in('M','F'):
            print("성별 등록이 완료 되었어요! 다음으로 넘어가요.")
            #custlist.append(customer)
            #print(custlist)
            break
        else:
            print("바르게 입력되지 않았어요 다시 입력해주세요")
            cRegistration
    while True:
        print(line)
        print("당신의 이메일을 등록해주세요")
        cRegistration = input()    

        #regex = re.complie('@')
        #golbang = regex.search(customer['email'])
        #if golbang != None:
        #break
        #else:
            #print('"@"를 포함한 정확한 이메일을 써주세요')
        for i in range(len(custlist)):
            #regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.]$[a-zA-Z]{2.3}')
            regex = re.compile("@")
            golbang = regex.search(cRegistration)               
            if  golbang == None or custlist[i]["email"] == cRegistration:
                print("메일이 잘못 되었어요.")
                break
        else:
            customer["email"] = cRegistration
            #custlist.append(customer)
            #print(custlist)
            print("이메일 등록이 완료됬어요! 다음으로 넘어가요!")
            break
    while True:
        print(line)
        print("당신의 생년월일을 등록해주세요!")
        cRegistration = input()
        if len(cRegistration) == 4:
            customer["birthday"] = cRegistration
            print("생년월일까지 등록이 모두 완료되었어요!")
            break
        else:
            print("생년월일을 바르게 입력해주세요")
            #cRegistration
    custlist.append(customer)
    global page 
    page +=1
    print(custlist)
    print(page)    
def curSearch():
    print("현재 고객 정보 조회")
    global page
    if page >= 0:
        print("지금 고객 정보는 {}번 고객님 입니다.".format(page+1))
        print(custlist[page])
    else:
        print("고객님 정보가 없습니다..")
def preSearch():
    print("이전 고객 정보 조회")
    global page
    if page <= 0:
        print("더 이상의 고객님 정보가 없습니다.")
    else:
        page -=1
        print(custlist[page])
        print("조회한 고객님 번호는 {}번 입니다.".format(page+1))
def nextSearch():
    print("다음 고객 정보 조회")
    #print(len(custlist))
    global page
    if page < len(custlist)-1:
        page +=1
        print(custlist[page])
        print("조회한 고객님 번호는 {}번 입니다.".format(page+1))
    else:
        print("더이상 고객님 정보는 없습니다.")
def deleteData():
    print("고객 정보 삭제")
    print(line)
    print("삭제할 고객님 이메일을 적어주세요.")
    cDelete = input()
    for i in range(len(custlist)):
        if custlist[i]["email"] == cDelete:
            del custlist[i]
            print("데이터 삭제완료")
            print(custlist)
            break
    else:
        print("삭제할 데이터가 없습니다.")
        #break       
def updateData():
    print("고객 정보 수정")
    print(line)
    default = 1
    print("수정할 고객의 이메일을 적어주세요.")
    while default:
        cUpdate = input()
        for i in range(len(custlist)):
            if custlist[i]["email"] == cUpdate:
                while True:  
                    Update = input("""
                    수정하실 부분을 선택해주세요
                    name = N
                    sex = S
                    email = E
                    brithday = B
                    종료 = exit
                    """)
                    if Update == "N":
                        while True:
                            print("수정할 이름을 입력해주세요.")
                            Nupdate = input()
                            if NumberCheck.match(Nupdate):
                                print("이름을 제대로 입력해주세요")
                            else:
                                custlist[i]["name"] = Nupdate
                                print("이름 수정완료")
                                break
                    elif Update == "S":
                        print("수정할 성별을 입력해주세요.")
                        while True:
                            Supdate = input().upper()
                            if Supdate in ("M","F"):
                                custlist[i]["sex"] = Supdate
                                print("성별 수정 완료")
                                print(custlist)
                                break
                            else:
                                print("존재할수 없는 성별입니다.다시 입력해줘요.")
                                #Supdate = input().upper()
                    elif Update == "E":
                        print("수정할 이메일을 입력해주세요")
                        check = 1
                        while check:
                            Eupdate = input()                                
                            for j in range(len(custlist)):
                                if custlist[j]["email"] == Eupdate:
                                    print("해당 이메일을 존재합니다. 다시 적으세요")
                                    break
                            else:
                                custlist[i]["email"] = Eupdate
                                print(custlist)
                                print("이메일 수정이 완료되었습니다.")
                                break
                            chekck = 0                                        
                    elif Update == "B":
                        print("수정할 생년월일을 입력해주세요.")
                        #custlist[i]["Birthday"] = input()
                        Bupdate = input()
                        if len(Bupdate) == 4 and NumberCheck.match(Bupdate):
                            custlist[i]["birthday"] = Bupdate
                            print("생년월일 수정이 완료되었습니다.")
                            print(custlist)
                        else:
                            print("생년월일이 올바르지 않습니다. 다시 입력하세요")
                    elif Update == "exit":
                        break
                    else:
                        print("제대로 입력해주세요.")
                else:
                    print("제대로 입력해주세요.")
                    break           
            default = 0 
            #print(custlist)

if __name__== "__main__":
    while True:
        choice = input("""
        다음 중에서 하실 일을 골라주세요:
        I  - 고객 정보 입력
        C - 현재 고객 정보 조회
        P - 이전 고객 정보 조회
        N - 다음 고객 정보 조회
        U - 고객 정보 수정
        D - 고객 정보 삭제
        Q - 프로그램 종료
        """)
        exe(choice)
        