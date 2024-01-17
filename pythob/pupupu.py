subjects = [
    "C++",
    "Java",
    "Python"
    ]
print(subjects)
print(subjects[::-1]) # ['Python', 'Java', 'C++'] 이 순간만 리스트를 바꾼다.
print(subjects) #['C++', 'Java', 'Python'] 리스트의 원본은 그대로 있음.
subjects.reverse() # 리스트의 원본 자체를 거꾸로 바꾼다.
print(subjects) # ['Python', 'Java', 'C++']

print()

subjects.append("NEW") #리스트의 '마지막'에 문자열을 추가한다.
print(subjects)
subjects.insert(2, "third") # 3번째 자리에 문자열을 추가적으로 집어넣는다.
print(subjects)

print()

subsubject = "Math", "Society"
print(subjects.append(subsubject))
print(subjects)
subjects[2] = "modified"
print(subjects)
print(subjects[-1])
del subjects[-1] #del(subjects[-1]) 또는 subjects.pop[-1]
#pop은 숫자 입력이 없으면 맨 뒤에서부터 지워버림.
print(subjects)

print()

# subjects.clear() # 전부 다 지워버림.
print("Java" in subjects) # Java가 subject 리스트 안에 있으면 True 없으면 False

friedns = ["H","P","L"]
print(friedns)
friedns.sort() #정렬하는 것이다. 원본을 바꾸는 것이다.
print(friedns)
friedns.sort(reverse=True)
print(friedns)
copy_subjects = sorted(subjects) # 정렬된 사본을 만들 때 sorted를 이용한다.
print(copy_subjects)
print(subjects)

#shallow copy & deep copy
