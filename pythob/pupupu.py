t0 = 5 #int
t1 = (5) #int
t2 = 5, #tuple
t3 = (5,) #tuple
t4 = (5, 7) #tuple
t5 = 5, 7 #tuple
print(type(t0),type(t1),type(t2),type(t3),type(t4),type(t5))
t6 = "python", "kim" # tuple packing
print(t6[1])
subject, prof = t6 # unpacking -> subject에는 python이 들어가고, prof에는 kim이 들어간다.
# #// packing과 unpackin의 개수가 같아야 한다. 다르면 ValueError

print(prof)

t7 = () # tuple
t8 = tuple() #tuple
t9 = 1, 2, 3
t10 = 3, 51235412
print(t9 == t10) # tuple간의 비교연산이 가능하다. -> 비교연산을 하면 False와 True로 return된다.
print(t9 > t10)
t11 = 4.43,
t12 = 3.97, 4.1, 3.27
print(id(t11))
t11 += t12
print(id(t11))
print(t11)
print(list('c a t . ,')) #문자열을 리스트 형태로 바꿨다.
print(list(t9)) # tuple은 변하지 않는 값이기 때문에 list로 바꾼 뒤 변화를 주고 다시 tuple로 만든다.
                # 이때 만들어진 tuple은 기존의 tuple과 메모리 저장된 곳이 다르다.