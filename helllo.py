year = "2020"
for i in range(1,4):
    print(int(year) - i)

letters = 'python'
print(letters[0:3:2] + "\t")

#Recursion 재귀함수.
def dive():
    return dive()

def factorial_repetition(n) -> int: # 팩토리얼 (결과 * i) 반복
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
print(factorial_repetition(int(input("number : "))))

def factorial_recursion(n):
    """
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function, int
    """
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1) # n * (n-1)!
number = int(input("nuber : "))
print(factorial_recursion(number))
print(factorial_repetition(number))
print(globals())

# 반복문은 속도가 매우 빠름. 재귀함수는 속도가 느리지만 가독성이 높고 실수할 확률이 적음.

#Async Function (ASYNCHRONOUS : 비동기화) // 다 다르게 움직이는 함수. -> 각자 할 일을 하니까 일처리 속도가 빨라짐.
# -> 동기화를 하면 속도가 느려짐. but


