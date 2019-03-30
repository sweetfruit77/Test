#  활용예제 map

arr = [1,2,3,4,5,6,7,8,9]
brr = list(filter(lambda x : x % 3 == 0,arr))
print(brr) #리스트 값으로 찍어낼때

for item in brr:
    print(item , end =" ") #일반 자료값으로 찍어낼때