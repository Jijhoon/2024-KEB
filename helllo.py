#(100°F-32) * 5/9 = 37.778°C 화씨를 섭씨로 바꾸기
print("If you want to exit, press write any word")
menu = input("1)Fahrenheit -> Celsius \n2)Celsius -> Fahrenheit \n3)Quit\n write what you want : ")
if menu == '1' :
    Fahrenheit = float(input('Input Fahrenheit : '))
    print(f'Fahrenheit : {Fahrenheit}F, Celsius : {((Fahrenheit-32.0) * 5/9):.4f}C')

elif menu == '2' :
    Celsius = float(input('Input Celsius : '))
    print(f'Celsius : {Celsius}C, Fahrenheit : {((Celsius*9/5) +32.0):.4f}F')

else :
    print('system is closed')