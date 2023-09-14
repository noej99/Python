# -*- coding:utf-8 -*-

# call by value, call by reference
d = 10
e = 10
############################
def test(a, b, c):
    print(a, b[0], c[0]) # 새로운 a, b, c
    a = 100 # 새로운 변수a에 넣기
    b[0] = 100 # 기존 변수b[0]에 넣기
    c = [100, 200] # 새로운 변수c에 넣기
    d = 100 # 4번줄 d가 아니고, 새로만든 d
    global e # 지금부터 쓰는 e는 밖에 있는 e(5번줄)
    e = 100
    print(a, b[0], c[0], d, e)
############################
a = 10
b = [10, 20]
c = [10, 20]
print(a, b[0], c[0], d, e)
test(a, b, c)
print(a, b[0], c[0], d, e) # 기존의 e는 GC로