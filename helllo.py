class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self, target):
        print(f"{self.name} attacked {target.name}!")

class Flame:
    def flamethrower(self,target):
        print(f"{self.name} use the skill 'Flamethrower' to {target}")
class Electric:
    def thunderbolt(self, target):
        print(f"{self.name} use the skill 'Thunderbolt' to {target}")
class Water:
    def water_Pulse(self, target):
        print(f"{self.name} use the skill 'Water Pulse' to {target}")
class Normal:
    def arm_Thrust(self, target):
        print(f"{self.name} use the skill 'Arm Thrust' to {target}")
class Dragon:
    def hyper_beam(self, target):
        print(f"{self.name} use the skill '	Hyper Beam' to {target}")

class Charmander(Pokemon, Flame):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

class Pikachu(Pokemon, Electric):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
class Squitle(Pokemon, Water):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
class Dialga(Pokemon, Dragon):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

class Mareep(Pokemon, Electric):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
class Octillery(Pokemon, Water):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
class Houndoom(Pokemon, Flame):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
class Snorlax(Pokemon, Normal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
class Rayquaza(Pokemon, Dragon):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

p1 = Charmander("Charmander", "Flame" )
p2 = Pikachu("Pikachu", "Electric" )
p3 = Squitle("Squitle", "Water" )
p4 = Dialga("Dialga", "Dragon" )

e1 = Mareep("Mareep", "Electric" )
e2 = Octillery("Octillery", "Water" )
e3 = Houndoom("Houndoom", "Flame" )
e4 = Snorlax("Snorlax", "Normal" )
e5 = Rayquaza("Rayquaza", "Dragon" )
print(p1)

Pokemon.attack(p1, e2)
flamethrower