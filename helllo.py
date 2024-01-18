#9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10).
# Use a for loop to find and print the third value returned.
def get_odds():
    for i in range(1, 10):
        if i % 2 == 1:
            yield i


for number in get_odds():
    print(number)

#9.3 Define a decorator called test that prints 'start' when a function is called, and 'end' when it finishes.

def test(f):
    def wrapper(*args, **kwargs):
        print("start")
        result = f(*args, **kwargs)
        print("end")
        return result
    return wrapper

@test
def func():
    return print("hi")
func()


def pupupu(arg,result = []):
    result.append(arg)
    return print(result)

pupupu("a")
pupupu("b")

def popopo(arg, result = None):
    if result is None:
        result = []
        result.append(arg)
    return print(result)

popopo("a")
popopo("b")

def ricecake(saysomething):
        def cake():
            return "I am delicious'%s'" % saysomething
        return cake

a = ricecake("hi") #이런 상태를 만들어야만 내부의 함수를 볼 수 있다. -> I am delicious'hi'
print(a())
print(ricecake("hi")) # >>> <function ricecake.<locals>.cake at 0x0000021B1EE0F420>

def newspaper(word):
    return print(word.capitalize() + "!")
newspaper("adlfjljksanfdlsa")

print("C:\\Windows")

list_ = {"naver", "kakao", "sk", "samsung"}

print("naver", "kakao", "sk", "samsung", sep=';')