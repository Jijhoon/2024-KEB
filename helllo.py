univ ="inha university"
counts_alphabet = {letter: univ.count(letter) for letter in univ}
print(counts_alphabet) # {'i': 3, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

#같은 결과 다른 방법 위에꺼는 dictionary의 축약형이 가능한 것을 보여준다.
counts_alphabet = dict()
for letter in univ:
    counts_alphabet[letter] = univ.count(letter)
print(counts_alphabet) # {'i': 3, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

# Assignment ex) 8.10
squares = {n: pow(n, 2) for n in range(10)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
#squares = {n: n**2 for n in range(10)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
#squares = {n: n*n for n in range(10)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(squares)
