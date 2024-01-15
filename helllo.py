#(100°F-32) * 5/9 = 37.778°C 화씨를 섭씨로 바꾸기
Fahrenheit = float(input('Input Fahrenheit : '))
print(f'Fahrenheit : {Fahrenheit}F, Celsius : {((Fahrenheit-32.0) * 5/9):.4f}C')

#문자열 타입으로 전환!
print(str(98.6))
print(str(1.0e4))

Hi= 'a, b, c, d' # Hi는 문자열의 공백을 포함한다.
print(Hi[1]), print(Hi[0]) #a=0 , 쉼표 공백 모두 자리를 차지하는 것이다. 이렇게 작성하면 줄바꿔서 작성됨
print(Hi[1],Hi[0]) # 이렇게 작성하면 한 줄에 작성되는데 여기에 띄어쓰기인 \n을 작성하면 오류가 발생함.
#\n 은 줄바꿈을 의미한다.
#For example
palindrome = 'A man,\nA plan,\nA canal: Panama.'
print(palindrome)
