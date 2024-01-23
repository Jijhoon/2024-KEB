import random

class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self, enemy):
        damage = random.randint(10, 20)
        print(f"{self.name} attacked {enemy}, causing {damage} damage!")
        try:
            e1.hp -= damage
            e2.hp -= damage
            e3.hp -= damage
            e4.hp -= damage
            e5.hp -= damage
            print(e1.hp, e2.hp, e3.hp, e4.hp, e5.hp) #???????????

        except:
            pass



class Endure:
    def hp(self, name, _type, hp):
        self.hp = hp


class Flame:
    def flamethrower(self,enemy):
        print(f"{self.name} used the skill 'Flamethrower' on {enemy}")
class Electric:
    def thunderbolt(self, enemy):
        print(f"{self.name} used the skill 'Thunderbolt' on {enemy}")
class Water:
    def water_Pulse(self, enemy):
        print(f"{self.name} used the skill 'Water Pulse' on {enemy}")
class Normal:
    def arm_Thrust(self, enemy):
        print(f"{self.name} used the skill 'Arm Thrust' on {enemy}")
class Dragon:
    def hyper_beam(self, enemy):
        print(f"{self.name} used the skill 'Hyper Beam' on {enemy}")

class Charmander(Pokemon, Flame, Endure):
    def __init__(self, name, _type, hp):
        super().__init__(name)
        self._type = _type
        self.hp = hp
class Pikachu(Pokemon, Electric, Endure):
    def __init__(self, name, _type, hp):
        super().__init__(name)
        self._type = _type
        self.hp = hp
class Squitle(Pokemon, Water, Endure):
    def __init__(self, name, _type, hp):
        super().__init__(name)
        self._type = _type
        self.hp = hp
class Dialga(Pokemon, Dragon, Endure):
    def __init__(self, name, _type, hp):
        super().__init__(name)
        self._type = _type
        self.hp = hp
class Mareep(Pokemon, Electric, Endure):
    def __init__(self, name, _type, hp):
        super().__init__(name)
        self._type = _type
        self.hp = hp
class Octillery(Pokemon, Water, Endure):
    def __init__(self, name, _type, hp):
        super().__init__(name)
        self._type = _type
        self.hp = hp
class Houndoom(Pokemon, Flame, Endure):
    def __init__(self, name, _type, hp):
        super().__init__(name)
        self._type = _type
        self.hp = hp
class Snorlax(Pokemon, Normal, Endure):
    def __init__(self, name, _type, hp):
        super().__init__(name)
        self._type = _type
        self.hp = hp
class Rayquaza(Pokemon, Dragon, Endure):
    def __init__(self, name, _type, hp):
        super().__init__(name)
        self._type = _type
        self.hp = int(hp)


p1 = Charmander("Charmander", "(Flame)", "40")
p2 = Pikachu("Pikachu", "(Electric)", "40")
p3 = Squitle("Squitle", "(Water)", "40")
p4 = Dialga("Dialga", "(Dragon)", "100")

e1 = Mareep("Mareep", "(Electric)", "30")
e2 = Octillery("Octillery", "(Water)", "30")
e3 = Houndoom("Houndoom", "(Flame)", "50")
e4 = Snorlax("Snorlax", "(Normal)", "60")
e5 = Rayquaza("Rayquaza", "(Dragon)", "80")

enemy = random.randint(1,5)
if enemy == 1:
    enemy = e1.name + e1._type + e1.hp
elif enemy == 2:
    enemy = e2.name + e2._type + e2.hp
elif enemy == 3:
    enemy = e3.name + e3._type + e3.hp
elif enemy == 4:
    enemy = e4.name + e4._type + e4.hp
elif enemy == 5:
    enemy = e5.name + e5._type + e5.hp

else:
    print("Rewrite the number.")
# print(p1.name + "(" + p1._type + ")")
# Flame.flamethrower(e3, p1)
# Pokemon.attack(p1, e2)
import os

if input("Press Enter to Continue \n"):
    next

print("Nice to meet you\n Could you tell me what your name is?")
master = input()

print(f"{master}... It's cool.\n")
print("I will tell you some information.\t"
      "You have 4 Pokemons\n"
      f"1) {p1.name + p1._type + p1.hp}\t"
      f"2) {p2.name + p2._type + p2.hp}\t"
      f"3) {p3.name + p3._type + p3.hp}\t"
      f"4) {p4.name + p4._type + p4.hp}\t"
      )
print("\n\nNow, let's go on a adventu`re")


selection = input("1)To the Forest 2)To the Jungle 3)To the Desert\n Where do you want to go? : ")
if int(selection) == 1:
    print(f"A wild {enemy} appeared in forest.")
elif int(selection) == 2:
    print(f"A wild {enemy} appeared in jungle.")
elif int(selection) == 3:
    print(f"A wild {enemy} appeared in desert.")

meeting = int(input("What will you do? \n1)Fight 2)Runway \n :"))
while True:
    if meeting == 1:
        battle = int(input(
            f"1) {p1.name + p1._type + p1.hp}\t"
            f"2) {p2.name + p2._type + p2.hp}\t"
            f"3) {p3.name + p3._type + p3.hp}\t"
            f"4) {p4.name + p4._type + p4.hp}\t"
            "Choose your pokemon! : "
            ))
        while battle == 1:
            battle1 = int(input("1)Attack 2)skill \n What is your next behavior? : "))
            if battle1 == 1:
                Pokemon.attack(p1, enemy)
                print(f"You did 15 damage to the {enemy}.")

            elif battle1 == 2:
                Flame.flamethrower(p1, enemy)

        while battle == 2:
            battle1 = int(input("1)Attack 2)skill \n What is your next behavior? : "))
            if battle1 == 1:
                Pokemon.attack(p2, enemy)
            elif battle1 == 2:
                Electric.thunderbolt(p2, enemy)

        while battle == 3:
            battle1 = int(input("1)Attack 2)skill \n What is your next behavior? : "))
            if battle1 == 1:
                Pokemon.attack(p3, enemy)
            elif battle1 == 2:
                Water.water_Pulse(p3, enemy)

        while battle == 4:
            battle1 = int(input("1)Attack 2)skill \n What is your next behavior? : "))
            if battle1 == 1:
                Pokemon.attack(p4, enemy)
            elif battle1 == 2:
                Dragon.hyper_beam(p4, enemy)



    else:
        print("You are lost...")
        break





