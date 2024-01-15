#문자열 추출하기
letter = "Hi nice to meet you. Try to break me"
print(letter[3:8]); print(letter[5:17:3]); print(letter[-1:2:-1])

#문자열 길이 len()
print('\n\n' + "the number of letter's length : "+str(len(letter))) # str을 안 붙이면 문자열 + 숫자가 되면서 오류가 발생하게 된다.

The_word = input("write any word : ")
print("How longest what you write? \n: "+ str(len(The_word)))

