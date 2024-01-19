class Pokemon:
    pass
    def __init__(self, name):
        self.name = name  #pikachu.name = "피카츄" , squirtle.name = "꼬부기" // 객체를 생성할 때 호출되는 영역.
        print(f"production of poketmonster of {name}") # pikachu = Pokemon("피카츄") 이렇게 넣어준다.
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")
pikachu = Pokemon("피카츄") # init은 각 개체마다 딱 한 번 이름을 지어주는 것이다.
squirtle = Pokemon("꼬부기")
charizard = Pokemon("리자몽")

pikachu.nemesis = squirtle
print(pikachu.name)
print(pikachu.nemesis.name)
print(squirtle.name)

# print()
# charizard.attack(squirtle)
#  # is a : 상속 관계 (Inherent) // has a : 연관 관계 // use a : 사용관계
class Pikachu(Pokemon): # is -a 피카츄는 포켓몬이다.
    pass
p1 = Pikachu("피카츄")
print(p1.name)

