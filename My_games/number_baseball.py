import random


class Digits_checker:
    def digit_check(self, user_try, game_digits):  # TODO: 유저가 입력한 숫자와 랜덤숫자의 자릿수가 다르다면 자릿수가 다르다고 출력. 같으면 strike ball out 출력.
        cnt_s = 0
        cnt_b = 0
        if user_input_digits != len(game_digits):
            return "The number of digits is different!"

        if user_try == game_digits:
            print(f"{user_name}, you win!!!\n Your score is ().\n CONGRATURAION!!")
            exit()    
        elif user_try != game_digits: #TODO: 지금은 하나라도 다를 떄 elif가 실행되는데 모두가 다를 때 OUT이 나오도록 만들어보자.
            for x in range(0, user_input_digits):
                if user_try[x] == game_digits[x]:
                    cnt_s += 1
                elif user_try[x] in game_digits:
                    cnt_b += 1
            return f"You have {cnt_s}-strike and {cnt_b}-ball!\n"
        
                         
                
            
            
            

if __name__ == "__main__":
    while True:
        start = input("Do you want to play number baseball game? (Y / N)\n:").casefold()
        if start.strip() == "y":
            break
        elif start.strip() == "n":
            exit()
        else:
            print("Please write the Y or N")
            continue

    user_name = input("Please input your nickname: ")

    while True:
        try:
            user_input_digits = int(input("How many digits of game do you want?: "))
            if user_input_digits > 0:
                break
            else:
                print("Please write a integer of plus")
        except:
            print("Please write a integer of plus")

    game_digits = [random.randint(0, 9) for i in range(user_input_digits)]
    game_digits[0] = random.randint(1, 9)  # NOTE: 게임에서 정한 랜덤 숫자리스트 = game_digits
    sequence = 1

    while True:
        print(game_digits)
        n = 0
        for i in range(0, 5):
            while True:
                n += 1
                if n == 1:
                    ordinal_number = "st"
                elif n == 2:
                    ordinal_number = "nd"
                elif n == 3:
                    ordinal_number = "rd"
                elif n >= 4:
                    ordinal_number = "th"
                if i == 1:
                    user_try = list(input(f"Your {sequence}{ordinal_number} attempt: "))
                    if len(user_try) != len(game_digits):
                        print("The number of digits is different!")
                        break
                    for i in range(0, user_input_digits):
                        user_try[i] = int(user_try[i].strip())
                    sequence += 1
                    checking = Digits_checker()
                    print(checking.digit_check(user_try, game_digits))

                elif i == 2:
                    user_try = list(input(f"Your {sequence}{ordinal_number} attempt: "))
                    if len(user_try) != len(game_digits):
                        print("The number of digits is different!")
                        break
                    for i in range(0, user_input_digits):
                        user_try[i] = int(user_try[i].strip())
                    sequence += 1
                    checking = Digits_checker()
                    print(checking.digit_check(user_try, game_digits))

                elif i == 3:
                    user_try = list(input(f"Your {sequence}{ordinal_number} attempt: "))
                    if len(user_try) != len(game_digits):
                        print("The number of digits is different!")
                        break
                    for i in range(0, user_input_digits):
                        user_try[i] = int(user_try[i].strip())
                    sequence += 1
                    checking = Digits_checker()
                    print(checking.digit_check(user_try, game_digits))
                else:
                    user_try = list(input(f"Your {sequence}{ordinal_number} attempt: "))
                    if len(user_try) != len(game_digits):
                        print("The number of digits is different!")
                        break
                    for i in range(0, user_input_digits):
                        user_try[i] = int(user_try[i].strip())
                    sequence += 1
                    checking = Digits_checker()
                    print(checking.digit_check(user_try, game_digits))
