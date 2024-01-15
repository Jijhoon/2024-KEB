
#"univ" = "inha university" // 불가능! literal : 소스코드의 고정된 값

# num = input("숫자 10을 입력해보시오 : ")
# if int(num) < 10:
#     print("too low")
# elif int(num) > 10:
#     print("too high")
# else :
#     print("correct") // 잘 작동한다.

    #같은 내용으로 바다코끼리 연산자를 사용가능하다
   # if (num := int(input("숫자 10을 입력해보삼 : "))) < 10:
   #     print("10보다 작은 숫자임")
   # else (num := int(input("숫자 10을 입력해보삼 : "))) > 10:
   #     print("10보다 큰 숫자임")
   #왜 인지 작동이 안된다..


#base_number = int(input("밑을 입력하시오 :"))
#exponent_number = int(input("지수를 입력하시오 :"))
#print(type(base_number), type(exponent_number))
# f -string
#print(f'밑은{base_number}, 지수는 {exponent_number}, 결과 값은 {pow(base_number ** exponent_number)}')
# format function
# rint('밑은 {0}, 지수는 {1}, 결과 값은 {2}')

# C언어에서는
#print('밑은 %d, 지수는 %d, 결과 값은 %d' % (base_number, exponent_number, pow(base_number, exponent_number)))


    l = [1,3,3,2,4,4] #list
    s = {1,3,3,2,4,4} #set
        print(l,s) # list : [1,3,3,2,4,4], set : {1,2,3,4}