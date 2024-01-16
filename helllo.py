# prime number
number = int(input("Input number : "))
is_prime = True # integer type -> bool
if number < 2:
    print(f'{number} is not prime number')
else:
    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False # remove +
            break
        #print(i, end=' ') # 계산하는 과정을 보여줌.
        i = i + 1

    if is_prime: # remove ==
        print(f'{number} is prime number')
    else:
        print(f'{number} is not prime number')