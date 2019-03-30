class StudentScore(object):
    def __init__(self,data):
        self._data = data
    
    def __len__(self):
        return len(self._data)
    
    def __contains__(self, d):
        if d in self._data:
            return True
        else:
            return False

if __name__ == "__main__":
    a1 = StudentScore([90,80,70,60])
    a2 = StudentScore([100,200,300,400,500])
    print(len(a1))
    print(90 in a1)
    print(65 in a1)
    print(a1 is a2)
    