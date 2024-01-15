dec = 65 #10 진수 (decimal)
octal = 0o101 #8 진수
hexadeciaml = 0x41 #16 진수
binary = 0b01000001 #2 진수
print(dec, octal, hexadeciaml, binary)
print(chr(binary)) #아스키코드로 보여주는 함수이다.
print(chr(dec), chr(octal), chr(hexadeciaml), chr(binary))
print(ord('B'), ord('Z'), ord('a'), ord('2')) #66, 90, 97, 50 아라비아 숫자는 48부터 시작한다 -> 0 = 48 / a 는 97 / A 는 65