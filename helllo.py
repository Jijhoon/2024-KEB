import random

class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self, enemy):
        print(f"{self.name} attacked {enemy}!")

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

class Charmander(Pokemon, Flame):
    def __init__(self, name, _type):
        super().__init__(name)
        self._type = _type
class Pikachu(Pokemon, Electric):
    def __init__(self, name, _type):
        super().__init__(name)
        self._type = _type
class Squitle(Pokemon, Water):
    def __init__(self, name, _type):
        super().__init__(name)
        self._type = _type
class Dialga(Pokemon, Dragon):
    def __init__(self, name, _type):
        super().__init__(name)
        self._type = _type

class Mareep(Pokemon, Electric):
    def __init__(self, name, _type):
        super().__init__(name)
        self._type = _type
class Octillery(Pokemon, Water):
    def __init__(self, name, _type):
        super().__init__(name)
        self._type = _type
class Houndoom(Pokemon, Flame):
    def __init__(self, name, _type):
        super().__init__(name)
        self._type = _type
class Snorlax(Pokemon, Normal):
    def __init__(self, name, _type):
        super().__init__(name)
        self._type = _type
class Rayquaza(Pokemon, Dragon):
    def __init__(self, name, _type):
        super().__init__(name)
        self._type = _type


p1 = Charmander("Charmander", "(Flame)" )
p2 = Pikachu("Pikachu", "(Electric)" )
p3 = Squitle("Squitle", "(Water)" )
p4 = Dialga("Dialga", "(Dragon)" )

e1 = Mareep("Mareep", "(Electric)" )
e2 = Octillery("Octillery", "(Water)" )
e3 = Houndoom("Houndoom", "(Flame)" )
e4 = Snorlax("Snorlax", "(Normal)" )
e5 = Rayquaza("Rayquaza", "(Dragon)" )

enemy = random.randint(1,5)
if enemy == 1:
    enemy = e1.name + e1._type
elif enemy == 2:
    enemy = e2.name + e2._type
elif enemy == 3:
    enemy = e3.name + e3._type
elif enemy == 4:
    enemy = e4.name + e4._type
elif enemy == 5:
    enemy = e5.name + e5._type

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
      f"1) {p1.name + p1._type}\t"
      f"2) {p2.name + p2._type}\t"
      f"3) {p3.name + p3._type}\t"
      f"4) {p4.name + p4._type}\t"
      )
print("\n\nNow, let's go on a adventu`re")
selection = input("1)To the Forest 2)To the Jungle 3)To the Desert\n Where do you want to go? : ")
if int(selection) == 1:
    print(f"A wild {enemy} appeared.")
elif int(selection) == 2:
    print(f"A wild {enemy} appeared.")
elif int(selection) == 3:
    print(f"A wild {enemy} appeared.")`

meeting = int(input("What will you do? \n1)Fight 2)Runway \n :"))
if meeting == 1:
    battle = int(input(
        f"1) {p1.name + p1._type}\t"
        f"2) {p2.name + p2._type}\t"
        f"3) {p3.name + p3._type}\t"
        f"4) {p4.name + p4._type}\t"
        "Choose your pokemon! : "
        ))
    while battle == 1:
        battle1 = int(input("1)Attack 2)skill \n What is your next behavior? : "))
        if battle1 == 1:
            Pokemon.attack(p1, enemy)
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





