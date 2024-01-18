empty_set = set() # 비어있는 set을 만드는 유일한 방법.
# print(set({'alphabet': 'A', 'country': 'Korea', 'fruits': 'Apple' })) # 순서개념이 존재하지 않는다. 그래서 랜덤의 순서로 나온다.
# print(set(("het", "hey", "what"))) # 순서개념이 존재하지 않는다. 그래서 랜덤의 순서로 나온다.
# print(set(("D", "A", "C", "B", "R", "T"))) # 순서개념이 존재하지 않는다. 그래서 랜덤의 순서로 나온다.
# print(set(dict[aaa:'c', b:"r", qq: "re"]))

a = {1, 2, 5}
b = {2, 3, 4}
print(a & b) # 교집합
print(a.intersection(a, b)) # 교집합

print(a.union(b)) # 합집합

print(a.difference(b)) # a - b 차집합

print(a^b) # 합집합 - 교집합 : 다르게 가지고 있는 값들.
print(a.symmetric_difference(b)) # # 합집합 - 교집합

freeze = frozenset([1, 5, 4, 32, 62, 34, 17, 134])
print(freeze) # frozenset({32, 1, 34, 4, 5, 134, 17, 62})
freeze = frozenset[1, 5, 4, 32, 62, 34, 17, 134]
print(freeze) # frozenset[1, 5, 4, 32, 62, 34, 17, 134]

freeze = frozenset(1, 5, 4, 32, 62, 34, 17, 134) # 이건 tuple로 인식되었다. 그래서 freeze는 1개인데 8개의 숫자가 와서 오류가 났다.
print(freeze)