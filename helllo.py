#university = r"Inha\nuniversity" # r(로스팅)을 문자열 앞에 붙이면 \n이 줄바꿈을 하지 않고 그대로 나오게 된다.
#print(university)

#number1 = str(input("first number :")) # str이 없다면 그냥 숫자끼리 더해짐.
#number2 = input("second number : ") # str() -> 문자열로 바꾸는 함수.
#print(number1, number2) # concatenation
#print(number1 * 3) #duplication
#print(number1 + 3) #type error -> 문자열 + 숫자.
#문자열을 추출할 때 교체를 하고 싶다!
name = "Henny"
name.replace( "H",  "P") # 이거는 안 바뀌는데?

print(name)
print("P" + name[1::1]) # [이상:미만:차례]!@!!!@!@!@!  이상(start) 미만(end) // 차례(step)는 0부터 X 1부터 시작한다.


