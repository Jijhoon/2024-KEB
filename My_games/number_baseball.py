import random
# Number Baseball Game (NBG)

        
class Checker():
    def __init__(self):
        self.check_strike()
        self.check_ball()
        self.out()

    def check_strike(t_n, digi):
        cnt_s = 0
        for i in range(0, digi):
            if list(range(digi))[i] == t_n[i]:
                cnt += 1
        print(cnt_s)

    def check_ball(t_n, digi):
        cnt_b = 0
        for i in range(0, digi):
            for y in range(0, digi):
                if (list(range(digi))[i] == t_n[y]) and (list(range(digi)) != t_n):
                    cnt_b += 1
        print(cnt_b)

    def out(t_n, b_n):
        if (b_n[i] != t_n[y]) and (b_n != t_n):
            print("You are out")

class Difference():
    def differ(self):
        self.__init__() 
        if (cnt_s >= 1) or (cnt_b >= 1):
            print(f"You have {check_strike()}-stirke and {check_ball()}-ball")
        else:    
            print(f"{out()}")

identifying = Checker()



    

while True:
    start = input("Do you want play the Game?(y / n)\n: ").casefold()

    if start.strip() == "y":
        break
    elif start.strip() == "n":
        print("Good bye")
        exit()
    else:
        print("Answer Y or N")

user_name = input("Write your nickname: ")

digits = int(input("How many digits of the game do you want?: ")) 
baseball_number = list(range(digits))
baseball_number[0] = random.randint(1, 9)
for i in range(1, len(baseball_number), ):
    baseball_number[i] = random.randint(0, 9)


while True: #TODO:점수가 0점이될때 false:
    try_number = list(input())
    attempt = 1
    try_number = list(input(f"The {attempt}st try : "))
    identifying()

    attempt += 1
    try_number = list(input(f"The {attempt}nd try : "))
    identifying()
    attempt += 1
    try_number = list(input(f"The {attempt}rd try : "))
    identifying()
    attempt += 1
    while True:
        try_number = list(input(f"The {attempt}th try : "))
        identifying()
        attempt += 1


