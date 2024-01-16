#for문
word = ("a1b2c3d")
for letter in word:
    print(letter)

print()  # 줄바꿈을 하게 한다.

univ =("inharkkrrm")
for letter in univ:
    print(letter, end=" ")

print()

for k in range(2, len(univ),3): #0부터 시작해서 1만큼의 step 생략가능 range(len(univ))
    print(univ[k], end=" ")