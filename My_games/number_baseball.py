import random


class Digits_checker:
    def digit_check(self, user_try, game_digits):
        cnt_s = 0
        cnt_b = 0
        if user_input_digits != len(game_digits):
            return "The number of digits is different!"

        if user_try == game_digits:
            print(
                f"{user_name}, you win!!!\n Your score is ().\n CONGRATURAION!!"
            )  # 점수 추가하기.
            exit()
        elif user_try != game_digits:
            for x in range(0, user_input_digits):
                if user_try[x] == game_digits[x]:
                    cnt_s += 1
                elif user_try[x] in game_digits:
                    cnt_b += 1
        if cnt_s == 0 and cnt_b == 0:
            return "OUT!\n"
        else:
            return f"You have {cnt_s}-strike and {cnt_b}-ball!\n"


sequence = 1
n = 1
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
                print("Please write a positive integer")
        except ValueError:
            print("Please write a positive integer")
    if user_input_digits >= 10:
        game_digits = [random.randint(0, 9) for i in range(user_input_digits)]
        game_digits[0] = random.randint(1, 9)  # NOTE: 게임에서 정한 랜덤 숫자리스트 = game_digits
    elif user_input_digits < 10:
        game_digits = [random.randint(0, 9) for i in range(user_input_digits)]
        game_digits[0] = random.randint(1, 9)
        for i in range(1, user_input_digits):
            while True:
                if game_digits[i] in game_digits[:i]:
                    game_digits[i] = random.randint(0, 9)
                else:
                    break

   
    while True:
        print(game_digits)

        for i in range(0, 5):
            while True:
                if n == 1:
                    ordinal_number = "st"
                elif n == 2:
                    ordinal_number = "nd"
                elif n == 3:
                    ordinal_number = "rd"
                elif n >= 4:
                    ordinal_number = "th"

                if i == 1:
                    user_try = list(
                        input(f"Your {sequence}{ordinal_number} attempt: ")
                    )  # TODO: 반복되는 것들을 함수로 처리하자.
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
                n += 1
