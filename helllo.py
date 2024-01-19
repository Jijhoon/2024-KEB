def desc(a):
    def wrapper(): # 내부의 함수는 별도의 공간을 가지고 있어서 외부함수를 그냥 실행시켜도 return되지 않음.
        print("booboobooboo")
        a()
    # print("a")
    return wrapper
 #desc()   #실행시키면 a만 나옴.
@desc
def something():
    print("do something")

something()
# s = desc(something) // 변수지정을 함으로써 내부의 함수를 작동시킬 수 있다. 내부함수는 외부함수에대한 정보를 받아들이는 것이다.
# s()