import re
import json
class Customer_management(object):
    def __init__(self):
        self.page = -1
        self.custlist =[]
        self.line = "="*40
        self.NumberCheck = re.compile('[0-9]+')
        self.TextCheck = re.compile('[a-z]+')
        default = 1
        while default:
            choice = input("""
            다음 중에서 하실 일을 골라주세요:
            I  - 고객 정보 입력
            C - 현재 고객 정보 조회
            P - 이전 고객 정보 조회
            N - 다음 고객 정보 조회
            U - 고객 정보 수정
            D - 고객 정보 삭제
            S - 고객 저장
            L - 고객 데이터 로드
            Q - 프로그램 종료
            """)   
            if choice == "I":
                self.insertData()
            elif choice == "C":
                self.curSearch()
            elif choice == "P":
                self.preSearch()
            elif choice == "N":
                self.nextSearch()
            elif choice == "U":
                self.updateData()
            elif choice == "D":
                self.deleteData()
            elif choice == "Q":
                default = 0
                self.exit()
            elif choice == "S":
                self.Save() 
            elif choice == "L":
                self.Load()
    def insertData(self):
        customer = {"name":"","sex":"","email":"","birthday":""}
        print("고객 정보 입력")
        while True:
            print("이름을 등록해주세요")
            cRegistration = input()
            if cRegistration == "" or self.NumberCheck.match(cRegistration):
                print("이름을 제대로 입력해주세요.")
                cRegistration
            else:
                customer["name"] = cRegistration
                print("이름이 등록 완료 됬어요! 멋진 이름이에요 다음으로 넘어가요")
                #custlist.append(customer)
                #print(custlist)
                break
        while True:
            print(self.line)
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
            print(self.line)
            print("당신의 이메일을 등록해주세요")
            cRegistration = input()    

            #regex = re.complie('@')
            #golbang = regex.search(customer['email'])
            #if golbang != None:
            #break
            #else:
                #print('"@"를 포함한 정확한 이메일을 써주세요')
            for i in range(len(self.custlist)):
                #regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.]$[a-zA-Z]{2.3}')
                regex = re.compile("@")
                golbang = regex.search(cRegistration)               
                if  golbang == None or self.custlist[i]["email"] == cRegistration:
                    print("메일이 잘못 되었어요.")
                    break
            else:
                customer["email"] = cRegistration
                #custlist.append(customer)
                #print(custlist)
                print("이메일 등록이 완료됬어요! 다음으로 넘어가요!")
                break
        while True:
            print(self.line)
            print("당신의 생년월일을 등록해주세요!")
            cRegistration = input()
            if len(cRegistration) == 4:
                customer["birthday"] = cRegistration
                print("생년월일까지 등록이 모두 완료되었어요!")
                break
            else:
                print("생년월일을 바르게 입력해주세요")
                #cRegistration
        self.custlist.append(customer)
        #global page 
        self.page +=1
        print(self.custlist)
        print(self.page)    

    def curSearch(self):
        print("현재 고객 정보 조회")
        #global page
        print(self.page)
        if self.page >= 0:
            print("지금 고객 정보는 {}번 고객님 입니다.".format(self.page+1))
            print(self.custlist[self.page])
        else:
            print("고객님 정보가 없습니다..")

    def preSearch(self):
        print("이전 고객 정보 조회")
        #global page
        if self.page <= 0:
            print("더 이상의 고객님 정보가 없습니다.")
        else:
            self.page -=1
            print(self.custlist[self.page])
            print("조회한 고객님 번호는 {}번 입니다.".format(self.page+1))

    def nextSearch(self):
        print("다음 고객 정보 조회")
        #print(len(custlist))
        #global page
        if self.page < len(self.custlist)-1:
            self.page +=1
            print(self.custlist[self.page])
            print("조회한 고객님 번호는 {}번 입니다.".format(self.page+1))
        else:
            print("더이상 고객님 정보는 없습니다.")

    def deleteData(self):
        print("고객 정보 삭제")
        print(self.line)
        print("삭제할 고객님 이메일을 적어주세요.")
        cDelete = input()
        for i in range(len(self.custlist)):
            if self.custlist[i]["email"] == cDelete:
                del self.custlist[i]
                print("데이터 삭제완료")
                print(self.custlist)
                break
        else:
            print("삭제할 데이터가 없습니다.")
            #break       
    def updateData(self):
        print("고객 정보 수정")
        print(self.line)
        default = 1
        print("수정할 고객의 이메일을 적어주세요.")
        while default:
            cUpdate = input()
            for i in range(len(self.custlist)):
                if self.custlist[i]["email"] == cUpdate:
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
                                if self.NumberCheck.match(Nupdate):
                                    print("이름을 제대로 입력해주세요")
                                else:
                                    self.custlist[i]["name"] = Nupdate
                                    print("이름 수정완료")
                                    break
                        elif Update == "S":
                            print("수정할 성별을 입력해주세요.")
                            while True:
                                Supdate = input().upper()
                                if Supdate in ("M","F"):
                                    self.custlist[i]["sex"] = Supdate
                                    print("성별 수정 완료")
                                    print(self.custlist)
                                    break
                                else:
                                    print("존재할수 없는 성별입니다.다시 입력해줘요.")
                                    #Supdate = input().upper()
                        elif Update == "E":
                            print("수정할 이메일을 입력해주세요")
                            check = 1
                            while check:
                                Eupdate = input()                                
                                for j in range(len(self.custlist)):
                                    if self.custlist[j]["email"] == Eupdate:
                                        print("해당 이메일을 존재합니다. 다시 적으세요")
                                        break
                                else:
                                    self.custlist[i]["email"] = Eupdate
                                    print(self.custlist)
                                    print("이메일 수정이 완료되었습니다.")
                                    break
                                chekck = 0                                        
                        elif Update == "B":
                            print("수정할 생년월일을 입력해주세요.")
                            #custlist[i]["Birthday"] = input()
                            Bupdate = input()
                            if len(Bupdate) == 4 and self.NumberCheck.match(Bupdate):
                                self.custlist[i]["birthday"] = Bupdate
                                print("생년월일 수정이 완료되었습니다.")
                                print(self.custlist)
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
    
    def exit(self):
        #print(self.custlist)
        result = self.custlist
        return result
    def Save(self):       
        json_making = json.dumps(self.custlist,ensure_ascii="utf-8",indent = 4)
        fp = open("custlist.txt","wt",encoding ="utf-8")
        fp.write("{}".format(json_making))
        fp.close()  
    def Load(self):
        fp = open("custlist.txt","rt",encoding ="utf-8")
        result = fp.read()
        #self.page +=1
        self.custlist = json.loads(result)
        for i in range(len(self.custlist)-1):
            self.page+=i
        
        fp.close()
if __name__ == "__main__":
    start = Customer_management()    
    