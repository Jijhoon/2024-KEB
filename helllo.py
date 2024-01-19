class Animal:
    def says(self):
        return '아이 엠 동물'
class Horse(Animal):
    pass

class Donkey(Animal):
    pass
class Mule(Donkey, Horse):
    pass
class Hinny(Horse, Donkey):
    # def says(self):
    #     return '버새 버새' # 없으면 계속 거슬러 올라간다.
    pass
m1 = Mule()
h1 = Hinny()
print(Hinny.__mro__)
print(h1.says())