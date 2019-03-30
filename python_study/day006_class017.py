# __str__ ->toString()의 개념이라 보면된다.
# __repr__ -> 문자열 전부를 표시.(?)

import random

class Dice(object):
    
    def __init__(self,start,end):
        self._start = start
        self._end = end
    
    def __call__(self):
        return random.randint(self._start , self._end)

if __name__ =="__main__":
    dice = Dice(1,6)
    print(dice())
    print(dice())
    print(dice())
    print(dice())