import random
# test = [1, 2, 3]
# len(3) -> 3자리 리스트
# number = list(input()) -> 문자열로된 리스트. 
# number = list(input())
# for i in range(0,len(number)):
#     number[i] = int(number[i])
# print(number)
a = map(list, input("input:"))
b = map(list, [1, 3, 5, 6])
for i in range(0, 4):
    a[i] = int(a[i])
if a in b:
    print("yes!")
else:
    print("No!")
