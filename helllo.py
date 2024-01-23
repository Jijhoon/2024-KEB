import random


class Pokemon:
    def __init__(self, name, pokemon_type, hp):
        self.name = name
        self.pokemon_type = pokemon_type
        self.hp = hp
        self.skills = []
        
    def get_info(self):
        return f"{self.name} {self.pokemon_type} {self.hp}"

    def attack(self, enemy):
        damage = random.randint(10, 20)
        print(f"{self.name} attacked {enemy}, causing {damage} damage!")
        try:
            enemy.hp -= damage

            print(f"{enemy} now has {enemy.hp} HP")
        except:
            pass
        

class Skill:
    def attack(self, enemy):
        pass

# TODO: 스킬 
class Flame(Skill): 
    def flamethrower(self, enemy):
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
    pass


class Pikachu(Pokemon, Electric):
    pass


class Squitle(Pokemon, Water):
    pass


class Dialga(Pokemon, Dragon):
    pass


class Mareep(Pokemon, Electric):
    pass


class Octillery(Pokemon, Water):
    pass


class Houndoom(Pokemon, Flame):
    pass


class Snorlax(Pokemon, Normal):
    pass


class Rayquaza(Pokemon, Dragon):
    pass


class Master:
    def __init__(self, name):
        self.name = name
        self.pokemons = [
            Charmander("Charmander", "(Flame)", "40"),
            Pikachu("Pikachu", "(Electric)", "40"),
            Squitle("Squitle", "(Water)", "40"),
            Dialga("Dialga", "(Dragon)", "100"),
        ]
    
    def show_pokemons(self):
        for pokemon in self.pokemons:
            print(f"{pokemon.name} {pokemon._type} {pokemon.hp}", end="\t")


def get_random_enemy():
    """Returns enemise ranmomly."""

    enemies = [
        Mareep("Mareep", "(Electric)", 30),
        Octillery("Octillery", "(Water)", 30),
        Houndoom("Houndoom", "(Flame)", 50),
        Snorlax("Snorlax", "(Normal)", 60),
        Rayquaza("Rayquaza", "(Dragon)", 80),
    ]
    return random.choice(enemies)


def main():
    if input("Press Enter to Continue \n"):
        next

    print("Nice to meet you\n Could you tell me what your name is?")
    name = input()
    print(f"{name}... It's cool.\n")
    master = Master(name)

    print("I will tell you some information.\t" "You have 4 Pokemons\n")
    master.show_pokemons()  
    print("Now, let's go on a adventure")

    selection = int(
        input(
            "1)To the Forest 2)To the Jungle 3)To the Desert\n Where do you want to go? : "
        )
    )

    placese = ["Forest", "Jungle", "Desert"]
    place = placese[selection - 1]

    enemy = get_random_enemy()

    print(f"A wild {enemy.get_info()} appeared in {place}")
    

    choice = int(input("What will you do? \n1)Fight 2)Runway \n :"))
    
    if choice == 1:
        master.show_pokemons()
        choice = int(input("Choose your pokemon! \n :"))
        pokemon = master.pokemons[choice - 1]
        
        while True:
            pass           
            
    elif choice == 2:
        print("You are lost...\n You lose...")
        return


if __name__ == "__main__":
    main()


# -------------------------------------------------------------------------
# FIXME: 아래부터 다 지움
# 1. 싸우면 포켓몬 하나 고르고-> 싸움-> 공격 기술 -> 적 피 닳게 하다가 피 0만들면 -> 게임승리 // 장소선택이후 도망 골르면 -> 게임패배
"""
while True:
    if meeting == 1:
        battle = int(
            input(
                f"1) {p1.name + p1._type + p1.hp}\t"
                f"2) {p2.name + p2._type + p2.hp}\t"
                f"3) {p3.name + p3._type + p3.hp}\t"
                f"4) {p4.name + p4._type + p4.hp}\t"
                "Choose your pokemon! : "
            )
        )
        while battle == 1:
            battle1 = int(input("1)Attack 2)skill \n What is your next behavior?: "))
            if battle1 == 1:
                Pokemon.attack(p1, enemy)

            elif battle1 == 2:
                Flame.flamethrower(p1, enemy)
            #  if enemy.hp <= 0:
            #     print("You win!!!")
            #     break  이걸 어디다 넣어야 할까ㅓ....

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
        print("You are lost...\n You lose...")
        break
"""