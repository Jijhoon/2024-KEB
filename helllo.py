#일반적으로는 keyword argument를 이용하지만
#positional argument
# argument : 인수 / 매개변수 : Parameters
# * : 가변 매개변수 // argue가 많을 때 그 만큼의 방을 제공해준다. 인수가 없으면 비어있는 튜플 등을 출력한다.
# *arg : optonal positional argument : 각 방에 맞게 순서대로 배치하기 때문에 positional
# **kwarg : optional keyword argument : 순서 상관없이 key에 맞게 value가 배치되기 때문에 keyword.

def a(n):
    if n is None:
        print(f"{n}: There is not space")
    elif a is True:
        print((f"{n}: There is space"))#???
    else:
        print((f"{n}: There is not itme in space"))

a("")
a(" ")
a([])
a([0])
a(0)
a(None)
a("true")
a(True)


def squares(*n):
    """
    넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    """
    return [pow(i, 2) for i in n ]

print(squares(5))

def run_function(f, number):
    return squares(number)
print(squares(8))
print(run_function(squares,9))

def new_run(f,*args) -> list:
    return f(*args)
print(new_run(squares,5, 6, 7))
