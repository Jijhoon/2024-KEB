#Split 문자열을 분리해서 리스트에 담는다 (매우 중요)
course = "2024 KEB bootcamp"
#print(course)
#list_course = course.split()   #['2024', 'KEB', 'bootcamp'] 띄어쓰기를 한 것을 기준으로 3개로 분리된다.
#list_course = course.split('B')   #['2024 KE', ' bootcamp'] B를 기준으로 나뉜다.
#print(list_course)

numbers = input("first_number second_number : ").split() #numbers : ["first_number", "second_number"]
#print(numbers[0] + numbers[1]) #concatenation 문자열이 더해진 상태가 된다.
print(int(numbers[0]) + int(numbers[1])) #arithmetic operation    [첫번째 방 + 두번째 방]

#Join 문자열 -> 리스트로 변환한다.
subjects = ["pyrhon", 'c++', "database"]
subjects_string = ' / '.join(subjects) #(공백)/(공백)을 사이에 끼워넣은 상태로 list안의 방들이 합쳐진다.
print("합쳐진 모습 : " + subjects_string) #합쳐진 모습 : pyrhon / c++ / database
