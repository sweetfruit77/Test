import re
def consol_ctr():
    custlist=[]                            
    page=-1
    line = "="*40
    NumberCheck = re.compile('[0-9]+')
    #TextCheck = re.compile('[a-z]+')
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
        if customer["sex"] == "M" or customer["sex"] == "F":
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
        for i in range(len(custlist)):   
            if  cRegistration == "" or custlist[i]["email"] == cRegistration:
                print("같은 메일이 존재합니다. 다시 등록해주세요")
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
    page += 1
    #print(custlist)
    print(page)
    return custlist

def consol_Vcc(customer):
    pass
    


if __name__ == "__main__":
    customer = consol_ctr()
    customer2 = consol_ctr()
    print(customer)
    print(customer2)
