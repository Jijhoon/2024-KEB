#prime number
number = int(input("Input number : "))
cnt = 0
i = 1
while i <= number:
    if number % i == 0:
        cnt = cnt + 1
    i = i + 1

if cnt == 2:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')

    # prime number
    number = int(input("Input number : "))
    cnt = 0
    i = 2
    while i < number:
        if number % i == 0:
            cnt = cnt + 1
            break
        print(i, end=' ') # 계산하는 과정을 보여줌.
        i = i + 1

    if cnt == 0:
        print(f'{number} is prime number')
    else:
        print(f'{number} is not prime number')