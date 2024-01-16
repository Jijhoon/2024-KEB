#replace 대체하기.
course = "2024 KEB bootcamp"
print(course)
print(course.replace('KEB', 'Inha'))
# 2024 Inha bootcamp // 여기서는 잠깐 변화된거다. course = course.replace()를 지정해줘야 완전 변화됨.
print(course) #2024 KEB bootcamp 다시 나타남

course = course.replace('KEB', 'Inha', 10) # 2024 Inha bootcamp // count는 up to 개념 ~개까지 교환
print(course)
#strip 양쪽의 공간제거. lstip 왼쪽의 공간제거. rstrip 오른쪽의 공간제거
world = "      earth        "
print(world)
print(world.strip())
new_world = "!!!!earth!!!!"
print(new_world)
print(new_world.strip('!'))
nice_world = "!@#$****@@!!#earth#!@#@!@#$@@***" #다른 언어가 한개라도 껴 있으면 제대로 안 지워진다. 예를들어 중간에 %, ^등이 껴잇으면 달라짐.
print(nice_world)
print(nice_world.strip("!#$@*"))

#순서찾는 함수 find, index // find는 찾지 못했을 때 -1을 출력 -> if문을 통해서 print 가능.
# index는 ValueError : substring not found        find와 index는 결과를 찾지 못했을 때 달라진다.
foem = "hello nice to meetddd sada you the coke fsdaasdasdasdasmellon here you are."
word = "the"
print(foem.find(word))# the는 앞에서부터 23번째이다.
print(foem.rfind(word))