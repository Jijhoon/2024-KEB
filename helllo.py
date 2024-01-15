# first_number = int(input("First number : "))
# second_number = int(input("Second number : "))
# quotient = first_number // second_number #몫
# remainder = first_number % second_number #나머지
# print(f'몫은 {quotient} 나머지는 {remainder}입니다.')

# 같은 코드를 쉽게 짜보자

first_number = int(input('First number : '))
second_number = int(input("Second number : "))
print(f'몫은 {divmod(first_number, second_number)[0]}, 나머지는 {divmod(first_number, second_number)[1]}입니다.')

first_number = int(input('First number : '))
second_number = int(input("Second number : "))
result = divmod(first_number, second_number)
print(f'몫은 {result[0]}, 나머지는 {result[1]}입니다.')