# -*- coding:utf-8 -*-
from random import randint

# Java
#    for : 반복횟수(0 ~ 10)
#    for-each : 컬렉션 탐색용
#    while : 반복조건
#    do-while : 반복조건(최소 1번은 반복 보장)

# jQuery
#    $.each(); : JS배열 대상 for + for-each
#    $(선택자).each(); : DOM객체 대상 for + for-each
#######################################################

# Python

# for-each

l = [1, 2, 3, 4, 5, 6, 7]
for v in l:
    print(v)
print("---------")
# list, set, dict, range, tuple, ...
# l2 = [0, 1, 2, 3, 4]
# l2 = range(5) # 0 ~ 4 range
# l2 = list(l2)
for v in range(5):
    print(v)
print("---------")

for v in range(10, 1, -1):
    print(v)
print("---------")

for v in range(2, 10):
    for l in range(1, 10):
        print("%d x %d = %d" %(v, l, l * v), end="\t")
    print()
print("---------")

# jQuery
# var ar = [1, 2, 3, 4]
# $.each(ar, function(i,v){

# });

l3 = ["a", "b", "c", "d", "e", "f"]
for i, v in enumerate(l3): # (인덱스, 값) tuple상태로
    print(i, type(i))
    print(v, type(v))
    print("------")
print("=========")

# dict(Map)
# 순서x, 키-값 쌍 => for랑은 기본적으로 연관x
d = {"기온": 30, "강수량":10, "습도": 100}

for k, v in d.items(): # (키, 값) tuple로
    print(k,type(k))
    print(v,type(v))
    print("------")
print("------------------------------")

# while

# 1 ~ 10랜덤, 5나오면 끝
# x = 0
while True:
    x = randint(1, 10)  # 1 ~ 10까지 정수 랜덤
    print(x)
    if x == 5:
        break
        # continue

# 반복문 속에서 변수 만들지 마시라
# -> Python(interpreter방식)에서는 안먹히는
# -> 효율적인 프로그램x, 개발용이o
print("---------")

# j가 3되면 전체가 끝나게
j3 = False
for i in range(6):
    for j in range(6):
        print(i, j)
        if j == 3:
            j3 = True
            break
    if j3:
        break
