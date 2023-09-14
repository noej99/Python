# -*- coding:utf-8 -*-

# ''' ''', """ """로 안의 글 형태를 유지하며 help로 내용을 불러올 수 있음(설명서용도?)

s = "글"
print(type(s))

s2 = """ 
ㅋㅋㅋ
 ㅋㅋㅋ
  ㅋㅋㅋ
   ㅋㅋㅋ
    ㅋㅋㅋ
     ㅋㅋㅋ
   """
   
print(s2)
print(type(s2))
print("----------")

class dog:
    '''
    짖는거
    '''
    def bark(self):
        print("멍")
help(print)
print("----------")

s = "자바때 하던 거"
# help(str)
print(s.startswith("자")) # '자'로 시작하나
print(s.replace("자바", "java")) # 자바 -> java
print(s[2]) # 세번쩨 글자
print(len(s)) # 총 글자 수
print(s.find("하던 거") != -1) # '하던 거'가 포함되나

s2 = "    가나다    "
print(s2.strip()) # 앞/뒤 띄어쓰기 없애기
s3 = "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ가나다ㅋㅋㅋㅋㅋㅋㅋㅋㅋ"
print(s3.strip("ㅋ")) # 앞/뒤 불필요한거 없애기

# String.format("%d", 10)
s4 = "키 : %d, 몸무게 : %d" %(180, 90)
print(s4)
#############################################
# 문자열 붙이기
# J : StringBuffer
# P : 메모리 효율-x
s5 = "가"
print(s5, id(s5))
s5 += "나"
print(s5, id(s5))
s5 += "다"
print(s5, id(s5))
#############################################
# 문자열 분리
# J : 
#    s6.split(",") -> [] -> 정형데이터에 유리
#    StringTokenizer -> while -> 비정형데이터에 유리
# P : split
s6 = "가,나,다"
s6list = s6.split(",")
for s66 in s6list:
    print(s66)










