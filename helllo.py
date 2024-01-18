def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)
print(outer(4, 6)) # 10

def out(word):
    def inn(quote):
        return "HiHi It's a nice day, '%s' "%quote
    return inn(word)

print(out(('MEMEME'))) #HiHi It's a nice day, 'MEMEME'

# def out_func(nout):
#     def inner_func(nin):
#         return nin * nin
#     return inner_func(nout)
# print(out_func(5))
#closures 안에 들어있는 함수의 주소를 가져옴. 변수 하나를 정해서 내부의 function으로 만들 수 있음.
def out_func(nout):
    def inner_func():
        return nout * nout
    return inner_func
x = out_func(9) #closures에서 중요한 것은 외부함수에서의 argument를 내부함수가 copy해서 작동한다는 것이다.
print(type(x)) #<class 'function'>

print()

print(x) #<function out_func.<locals>.inner_func at 0x0000025B348EF060>

print()

print(x()) #81 -> x는 함수이기 때문에 소괄호를 포함해야 작동한다.

numbes = ["-7", "11", "3"]
print(sum(map(int, numbes)))

#같은 결과 더 긴 방법
numbes = ["-7", "11", "3"]
hap = 0
for number in numbes:
    hap = hap + int(number)
print(hap)