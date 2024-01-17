sugang = dict(python = "kim", cpp = "sung", db = "kang")
# print(sugang)
# sugang['datastructure'] = 'kim' # key와 value를 추가함.
# print(sugang)
# sugang['datastructure'] = 'park' #update
# print(sugang)
# print(sugang['db'])
# print(sugang.get('db'))
# print(sugang.get('opensource', 'not exist')) #앞에 있는 key가 dict에 존재하지 않을 때 뒤에 있는 값을 return함 있으면 value 나옴.
for subject, professor in sugang.items(): # 순서는 다르게 나올지 몰라도 두개를 같이 추출.
    print(f'{subject}과목 담당교수는 {professor}입니다.')

for k in sugang.keys(): # key만 추출
    print(k)

print()

for v in sugang.values(): # value만 추출
    print(v)

for s in sugang.items(): # tuple로 return
    print(s)