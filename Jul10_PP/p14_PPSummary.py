# -*- coding:utf-8 -*-
from random import randint

# 1. 가위
# 2. 바위
# 3. 보
# ------------
# 뭐 : 2
# 컴 : 가위
# 나 : 바위
# 승
# ------------ 질때까지 반복
# ?연승

##############################################
# 함수

def printRule():
    for i, h in enumerate(handTable):
        if i != 0:
            print("%d) %s"% (i, h))

def userFire():
    uh = int(input("뭐 : "))
    if 1 <= uh <= 3:
        return uh
    return userFire()

def comFire():
    return randint(1, 3)

def printHand(): # 함수안에 넣지 않아도 interpreter방식이므로 그 전에 들어갈 변수가 있다면 자동으로 넣어짐
    print("컴 : %s"% handTable[com])
    print("나 : %s"% handTable[me])
    
def judge():
    t = me - com
    if t == 0:
        print("무승부")
        print("----------")
        return 0    
    elif t == -1 or t == 2:
        print("패")
        print("----------")
        return 123456
    else:
        print("승")
        print("----------")    
        return 1
    
##############################################
handTable, win = [None, "가위", "바위", "보"], 0

printRule()

#메인

# handTable = [None, "가위", "바위", "보"]

# for i, h in enumerate(handTable):
#     if i != 0:
#         print("%d) %s"% (i, h))

# print("1) 가위")
# print("2) 바위")
# print("3) 보")
print("----------")    
# win = 0
# x = {1:"가위", 2:"바위", 3:"보"}
while True:
#     me = int(input("뭐 : "))
#     com = randint(1,3)
    me, com = userFire(), comFire()
#     print("컴 : %s"% handTable[com])
#     print("나 : %s"% handTable[me])
    printHand()
#     t = me - com
#     if t == 0:
#         print("무승부")
#         print("----------")    
#     elif t == -1 or t == 2:
#         print("패")
#         print("----------")
#         break
#     else:
#         print("승")
#         win += 1
#         print("----------") 
    result = judge()
    if result == 123456:
        break
    win += result
print("%d연승"% win)  

