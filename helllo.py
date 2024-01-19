class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self, target):
        print(f"{self.name} attacked {target.name}!")

class Flame:
    def flamethrower(self,target):
        print(f"{self.name} used the skill 'Flamethrower' on {target.name}")
class Electric:
    def thunderbolt(self, target):
        print(f"{self.name} used the skill 'Thunderbolt' on {target.name}")
class Water:
    def water_Pulse(self, target):
        print(f"{self.name} used the skill 'Water Pulse' on {target.name}")
class Normal:
    def arm_Thrust(self, target):
        print(f"{self.name} used the skill 'Arm Thrust' on {target.name}")
class Dragon:
    def hyper_beam(self, target):
        print(f"{self.name} used the skill 'Hyper Beam' on {target.name}")

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
        super().__init__(_type)

p1 = Charmander("Charmander", "Flame" )
p2 = Pikachu("Pikachu", "Electric" )
p3 = Squitle("Squitle", "Water" )
p4 = Dialga("Dialga", "Dragon" )

e1 = Mareep("Mareep", "Electric" )
e2 = Octillery("Octillery", "Water" )
e3 = Houndoom("Houndoom", "Flame" )
e4 = Snorlax("Snorlax", "Normal" )
e5 = Rayquaza("Rayquaza", "Dragon" )

print(p1.name + "(" + p1._type + ")")
# Flame.flamethrower(e3, p1)
# Pokemon.attack(p1, e2)
import os

if input("Press Enter to Continue \n"):
    next

print("Nice to meet you\n Could you tell me what your name is?")
master = input()

print(f"{master}... It's cool. ")
print()
print("I will tell you some information."
      "You have 4 Pokemons\n"
      f"1) {p1.name + '(' + p1._type + ')'}\t"
      f"2) {p2.name + '(' + p2._type + ')'}\t"
      f"3) {p3.name + '(' + p3._type + ')'}\t"
      f"4) {p4.name + '(' + p4._type + ')'}\t"
      )