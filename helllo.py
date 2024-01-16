subject = "python c++ database linux"
while True :
    word = input("press the word : ")
    if subject.find(word) == -1:
        print("다시 입력하시오")
    else :
        print(subject.find(word));
        break
# index는 값을 찾지 못하면 결과 값이 Error이다. vs find는 값을 찾지 못하면 결과 값이 -1이다.
##preview
#try:
#    print(~~)
#except ValueError :
#count 함수 : 몇 개 있는 지 알려준다.

#is 는 True 또는 False를 return한다.
