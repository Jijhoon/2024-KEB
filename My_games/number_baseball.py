import random


class Digits_checker:
    def digit_check(user_try):  # TODO: 유저가 입력한 숫자와 랜덤숫자의 자릿수가 다르다면 자릿수가 다르다고 출력. 같으면 strike ball out 출력.
        cnt_s = 1
        for i in range(i, user_input_digits):
            if user_try[i] == game_digits[i]:
                cnt_s += 1
                return cnt_s
        cnt_b = 1
        for x in range(x, user_input_digits):
            for y in range(y, user_input_digits):
                if (user_try[x] == game_digits[y]) and (user_try[x] != game_digits[x]):
                    cnt_b += 1
                    return cnt_b
        for x in range(x, user_input_digits):
            for y in range(y, user_input_digits):
                if (user_try[x] != game_digits[y]) and (user_try[x] != game_digits[x]):
                    return "OUT!"


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
        attempt = Digits_checker()
        for i in range(0, 3):
            for n in range(1, 10):
                if n == 1:
                    ordinal_number = "st"
                elif n == 2:
                    ordinal_number = "nd"
                elif n == 3:
                    ordinal_number = "rd"
                else:
                    ordinal_number = "th"
            if i == 1:
                print(game_digits)
                user_try = list(input(f"Your {sequence}{ordinal_number} attempt: "))
                for i in range(0, user_input_digits):
                    user_try[i] = int(user_try[i])
                sequence += 1
                attempt.digit_check(user_try)

            elif i == 2:
                ordinal_number = "nd"
                user_try = list(input(f"Your {sequence}{ordinal_number} attempt: "))
                for i in range(0, user_input_digits):
                    user_try[i] = int(user_try[i])
                sequence += 1
                attempt.digit_check(user_try)
            elif i == 3:
                ordinal_number = "rd"
                user_try = list(input(f"Your {sequence}{ordinal_number} attempt: "))
                for i in range(0, user_input_digits):
                    user_try[i] = int(user_try[i])
                sequence += 1
                attempt.digit_check(user_try)
            else:
                user_try = list(input(f"Your {sequence}{ordinal_number} attempt: "))
                for i in range(0, user_input_digits):
                    user_try[i] = int(user_try[i])
                sequence += 1
                attempt.digit_check(user_try)
