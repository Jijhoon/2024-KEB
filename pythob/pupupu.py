import copy
subjects = ["a", ["b", "c"],  "d"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(a)
print(subjects, a, b, c, d, e)
subjects[1][1] = "x"
print(subjects, a, b, c, d, e)
#deep copy 새로운 메모리 공간을 줘서 원본을 바꿔도 더 이상 바뀌지 않음.
#[expression for item in iterable] 정말 많이 사용한다!
number_list = [number for number in range(1,6)]
print(number_list)

squares = list()
squares.append(1*1)
print(squares)

square = list()
for i in range (1, 5, 1):
    squares.append(i*i)
print(square)

#  i*i for in range(1, 6, 1):

