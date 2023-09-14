# -*- coding:utf-8 -*-

# J
#    wrapperClass : 기본형에 해당하는 객체(int -> Integer)
#                   객체형이 필요할때(list<Integer>)
#                   형변환(Integer.parseInt("1"))
# P
#    기본형이 없고, wrapperClass만 쓰는 중
#    객체형밖에 없고
#    형변환은 생성자로

a = "10"
a = int(a)
print("---------------")
# 숫자(x, y, z, ...) :

data = input("숫자(x, y, z, ...) : ")
data = data.split(",")
hab = 0
for n in data:
    try:
        hab += int(n)
    except:
        pass
print(hab)
