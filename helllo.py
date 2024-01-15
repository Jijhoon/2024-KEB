letter = input('Input alphabet letter : ')
# vowels = {'a', 'e', 'i', 'o','u'} // set. set은 바꿀수 없는 가변상태로 되어있다.
vowels = "aeiou" # str 이경우에는 중간 문자를 바꿀 수 있다.
print(type(vowels))
if letter in vowels : # in이 함수가 되는 것이다.
    print(f'{letter} is a vowel!')
else :
    print(f'{letter} is a consonant!')


