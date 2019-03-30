from airforce import Airforce

class Bomber(Airforce):
    def __init__(self,bomber_num):
        self._bomber_num = bomber_num
    
    def take_off(self):
        print("폭격기 발진")

    def fly(self):
        print("폭격기 목적지로 출격")

    def attack(self):
        for i in range(self._bomber_num):
            print("폭탄투하")
            self._bomber_num -= i
    def land(self):
        print("폭격기 착륙")

if __name__ =="__main__":
    B = Bomber(10)
    B.take_off()
    B.fly()
    B.attack()
    B.land()