# -*- coding:utf-8 -*-

# Java : 규칙 -> 소스보기 편함
#        저급언어 -> 컴 친화적(효율적인 프로그램)
# Python : 자유 -> 복잡
#        고급언어 -> 사람 친화적(개발 편함)

# Java : 저급 언어(사람이 컨트롤)
#    데이터 특징 파악해서 최적의 자료형 찾기

# Python : 고급언어(언어 자체적으로 자동 처리)
#    자료형 자동
#    기본형x, 전부 다 객체

# Python의 int == Java의 Integer(int 아님)
a = 10       # Object a = new Integer(10);
print(a)
print(type(a)) # 자료형 확인
print(id(a))  # heap영역의 주소값

a = "ㅋ"     # a = new String("ㅋ");
print(a)
print(type(a))
print(id(a))

# interpreter
# Java시절에 변수 사용범위가 어쩌고.. - x
# 그 변수 쓰는 시점에 그 변수가 있기만 하면 o
a = 20
if (a > 10):
    b = 30
print(b)
