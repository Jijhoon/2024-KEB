
#"univ" = "inha university" // 불가능! literal : 소스코드의 고정된 값

num = input("숫자 10을 입력해보시오 : ")
if int(num) < 10:
    print("too low")
elif int(num) > 10:
    print("too high")
else :
    print("correct")


    #같은 내용으로 바다코끼리 연산자를 사용가능하다
   # if (num := int(input("숫자 10을 입력해보삼 : "))) < 10:
   #     print("10보다 작은 숫자임")
   # else (num := int(input("숫자 10을 입력해보삼 : "))) > 10:
   #     print("10보다 큰 숫자임")
   #왜 인지 작동이 안된다..