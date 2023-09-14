# -*- coding:utf-8 -*-

# 이클립스
# Python : 들여쓰기가 문법이라
# ctrl + shift + f 별로
name = input("이름 : ")
height = float(input("키 : "))
age = int(input("나이 : "))
print("---------------------")
print("키는 %.1fcm, 나이는 %d살" % (height, age))

# 키가 150이상
a = (height >= 150)
print(a)

# Java : 연산자는 stack영역이 대상
# Python : 기본형이 없 -> stack에 데이터 없 -> ?
#        알아서 적절히 돌아가게 되어있음

# 이름이 홍길동
b = (name == "홍길동")
print(b)
# and(&&), &(안맞아도 끝까지 가는거)
# or(||), |
# ^(xor : 조건중 하나만 맞는경우)
# and, or
# 키가 100넘고, 나이가 80넘으면
c = (age > 80) and (height > 100)
print(c)

# 키가 100넘든지, 나이가 80넘든지 하나만
d = (height > 100) ^ (age > 80)
print(d)

# 20대만 (20 <= age <= 29)
# e = (age < 30) and (age > 19)
e = (19 < age < 30)
print(e)

# 나이가 20살 이상이면 어서오세요, 아니면 나가
# f = (age >= 20) ? "어서오세요" : "나가"
# print(f)
if (age >= 20):
    print("어서오세요")
else:
    print("나가")

print(10 << 2)