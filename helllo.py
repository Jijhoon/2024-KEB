class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 납니다."


class SwmmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."


class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self):
        print("공격!")
    def get_name(self):
        print("inside getter")
        return self.name
    def set_name(self, new_name):
        print("inside setter!!!")
        self.name = new_name
class Charizard(Pokemon, FlyingMixin):
    pass
class Gyarados(Pokemon, SwmmingMixin):
    pass
g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
print(c1.fly())
print(g1.swim())
print(g1.name)
g1.set_name("잉어킹")
print(g1.name)
c1.attack()
Charizard.attack(c1)
#Charizard.attack() # Charizard는 class 명이기 때문에 오류가 발생 객체명인 c1이 와야 실행이 된다.
