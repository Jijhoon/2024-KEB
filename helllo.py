#lambda : 영구적인 함수 // 자주쓰는 함수라서 미리 만들어 놓는다.
def squares(n):
    return n * n
even_numbers = [i for i in range(51) if i % 2 == 0]
print(even_numbers)
print(tuple(map(squares, even_numbers)))
print(tuple(map(lambda x: x**2, even_numbers)))

# 구조 >>> lambda input: input이 실행되는 식.

# generator는 메모리에 저장하지 않는다. 숫자 생성하고 다음숫자 생성할때 이전 숫자를 지워버린다. ex) range()

def my_range(first = 0, last = 5, step = 1):
    number = first
    while number < last:
        yield number #함수의 실행 상태를 유지하면서 값을 순차적으로 반환 // 큰 데이터를 처리할 때 메모리를 효율적으로 사용
        number += step
r = my_range()
print(r,type(r))

for x in r : # 0~4까지 출력됨.
    print(x)
for x in r: #한번 사용한 값들이기 때문에 휘발해버렸음.
    print(x)

#Decorators  OCP 개방폐쇄원칙(open closed principle) : 확장에는 열려있고 수정에는 닫혀야한다.
#document_it() // 함수 출력과 인수 출력을 해준다.

# decorator
def description(f):  # closure
    def inner(*args):
        print(f.__name__)
        print(f.__doc__)
        r = f(*args)
        return r

    return inner


def squares(n):
    """
    제곱 함수
    """
    return n * n

@description # 얘가 붙음으로써 데코레이팅이 된다.
def power(b, e):
    """
    거듭제곱 함수
    """
    result = 1
    for _ in range(e):
        result = result * b
    return result


f1 = description(squares)
print(f1(9))
print(power(2, 10))
# f2 = description(power)
# print(f2(2, 10))
