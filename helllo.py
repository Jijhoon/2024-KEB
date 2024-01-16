#isalnum() : 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되었는지 확인하는 파이썬 문자열 메소드
subject = "pythoncadataba!!!!se123linux"
print(subject.isalnum()) #False 느낌표가 존재하기 때문에 False가 return되었다.
subject = "python cad ataba e123linux"
print(subject.isalnum()) #False 공백이 존재하기 때문에 False가 return되었다.
subject = "pythoncadatabae123linux"
print(subject.isalnum()) #True 문자열이 알파벳과 숫자로만 이루어졌기 때문이 True가 return되었다.

setup = "....sdafadsf....dsadsafsd ...."
print(setup.strip(".")) # 앞 뒤로 붙은 ... 만 없애기 때문에 중간 부분의 ...이 없어지지 않음.

#capitalize() : 대문자로 바꾼다.
print(setup.capitalize())
print(setup.title())
#정렬. 배치
print(setup)
# %s : string(문자열) / %x : 16진수 / %o : 8진수 / %d : decimal(십진수) / %f : float(실수형) / %e : 지수형  / %g : 실수형 자동출력
# cf) int : 정수형 integer


