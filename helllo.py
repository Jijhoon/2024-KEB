#(100°F-32) * 5/9 = 37.778°C 화씨를 섭씨로 바꾸기

while True :
    menu = input(
        "\n\n1)Fahrenheit -> Celsius "
        "\n2)Celsius -> Fahrenheit "
        "\n3)Quit\n write what you want : "
        )
    if menu == '1' :
        Fahrenheit = float(input('Input Fahrenheit : '))
        print(
            f'\nFahrenheit : {Fahrenheit}F, '
            f'Celsius : {((Fahrenheit-32.0) * 5/9):.4f}C'
            )
        print(menu)
    elif menu == '2' :
        Celsius = float(input('Input Celsius : '))
        print(
            f'\nCelsius : {Celsius}C, '
            f'Fahrenheit : {((Celsius*9/5) +32.0):.4f}F'
            )
        print(menu)
    elif menu == '3':
        print("Good Bye! See you again"); break
    else :
        print('You write the wrong number. Try again!')



