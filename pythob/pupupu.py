#Number Guessing Game
import random
user_name = input("Write your name : ")
number = random.randint(1,100)
print("We will play the game.\nGuess the number,1 to 100")
try_op = 0
while try_op < 7:
    try_op += 1
    try:
        i = int(input("number what you expected : "))

        if isinstance(i,int):
            if number < i:
                print("\nIt's too high!")
            elif number > i:
                print("\nIt's too low!")
            elif number == i:
                break
        else:
            print("system error")
    except ValueError:
        print("\nThat's wrong way! You lost one chance!")
if number == i:
    print(f"\ncongratulation! {user_name}, you win!")
else:
    print(f"\nYou lose, {user_name}. The answer was {number}. Try next time!")