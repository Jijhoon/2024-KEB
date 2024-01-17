while True :
    menu = input(
        "\n\n1)Fahrenheit -> Celsius "
        "\n2)Celsius -> Fahrenheit "
        "\n3)check the prime number"
        "\n4)check the prime number of section"
        "\n5)quit"
        "\nwrite what you want : "
        )
    if menu == '1' :
        Fahrenheit = float(input('Input Fahrenheit : '))
        print(f'\nFahrenheit : {Fahrenheit}F, Celsius : {((Fahrenheit-32.0) * 5/9):.4f}C')
        print(menu)
    elif menu == '2' :
        Celsius = float(input('Input Celsius : '))
        print(f'\nCelsius : {Celsius}C, Fahrenheit : {((Celsius*9/5) +32.0):.4f}F')
        print(menu)
    elif menu == '3':
       number = int(input("press any number: "))
       is_prime = True
       if number < 2:
           print(f"{number} is NOT prime number")
       else :
           for i in range(2, number):
               if number % i == 0:
                   is_prime = False

           if is_prime:
               print(f"{number}is prime number")
           else:
               print(f"{number}is NOT prime number")

    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                # pass
                continue
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime: print(number, end=' ')
        print()
    elif menu == '5':
        print('Terminate Program.')
        break


    else:
        print('You write the wrong number. Try again!')
