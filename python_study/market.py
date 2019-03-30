import re
class Market(object):
    Numbercheck = re.compile('[0-9]+')
    #Confirm2 = re.compile('[a-zA-Z]+')
    market_product = {"라면":100,"과자":100,"고기":100,"생선":100,"장난감":100}
    def __init__(self):    
        default = 1
    
        while default:
            choice = input("""
            회원분은 다음 화면으로 로그인해주세요
            customer = C
            manager = M
            종료 = Q
            """).upper()
            if choice == "C":
                self.Customer()
            elif choice == "M":
                self.manager()
            elif choice == "Q":
                default = 0
                #quit()
            else:
                print("잘못된 입력 형식입니다.")
    def Customer(self):
        print("손님 온라인마켓에입장해주셔서 감사합니다.!")
        while True:
            choice2 = input("""
            무엇을 원하십니까?
            상품구매 = P
            종료 = Q
            """)
            if choice2 == "Q":
                print("감사합니다 손님 또 방문해주세요!")
                quit()
            elif choice2 == "P":
                print("상품구매로 이동합니다.")
                self.Purchase()
    def manager(self):
        print("매니저 무엇을 원하십니까!")

    def Purchase(self):
        print("상품목록")
        print(list(self.market_product.keys()))
        while True:
            choice3 = input("""
            상품선택
            라면 = L
            과자 = S
            고기 = M
            생선 = F
            장난감 = T
            구매종료 = Q
            """)
            if choice3 == "L":
                while True:
                    print("구매할 수량을 입력해주세요.")
                    Quantity = input()
                    if Quantity != "" and self.Numbercheck.match(Quantity) and self.market_product["라면"] >= int(Quantity):
                        self.market_product["라면"] -= int(Quantity)
                        print("라면을 구매하셨습니다.")
                        print(list(self.market_product.items()))
                        break
                    else:
                        print("현재입고 수량을 초과했거나 잘못된 방식으로 다시적어주세요 입력하셨습니다.")
                        Quantity   
            elif choice3 == "S":
                while True:
                    print("구매할 수량을 입력해주세요.")
                    Quantity = input()
                    if Quantity != "" and self.Numbercheck.match(Quantity) and self.market_product["과자"] >= int(Quantity):
                        self.market_product["과자"] -= int(Quantity)
                        print("과자를 구매하셨습니다.")
                        print(list(self.market_product.items()))
                        break
                    else:
                        print("현재입고 수량을 초과했거나 잘못된 방식으로 다시적어주세요 입력하셨습니다.")
                        Quantity
            elif choice3 == "M":
                while True:
                    print("구매할 수량을 입력해주세요.")
                    Quantity = input()
                    if Quantity != "" and self.Numbercheck.match(Quantity) and self.market_product["고기"] >= int(Quantity):
                        self.market_product["고기"] -= int(Quantity)
                        print("고기를 구매하셨습니다.")
                        print(list(self.market_product.items()))
                        break
                    else:
                        print("현재입고 수량을 초과했거나 잘못된 방식으로 다시적어주세요 입력하셨습니다.")
                        Quantity
            elif choice3 =="F":
                while True:
                    print("구매할 수량을 입력해주세요.")
                    Quantity = input()
                    if Quantity != "" and self.Numbercheck.match(Quantity) and self.market_product["생선"] >= int(Quantity):
                        self.market_product["생선"] -= int(Quantity)
                        print("생선을 구매하셨습니다.")
                        print(list(self.market_product.items()))
                        break
                    else:
                        print("현재입고 수량을 초과했거나 잘못된 방식으로 다시적어주세요 입력하셨습니다.")
                        Quantity
            elif choice3 == "T":
                while True:
                    print("구매할 수량을 입력해주세요.")
                    Quantity = input()
                    if Quantity != "" and self.Numbercheck.match(Quantity) and self.market_product["장난감"] >= int(Quantity):
                        self.market_product["장난감"] -= int(Quantity)
                        print("장난감을 구매하셨습니다.")
                        print(list(self.market_product.items()))
                        break
                    else:
                        print("현재입고 수량을 초과했거나 잘못된 방식으로 다시적어주세요 입력하셨습니다.")
                        Quantity
            elif choice3 == "Q":
                break
if __name__ == "__main__":
   Market()