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