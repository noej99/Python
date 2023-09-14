# -*- coding:utf-8 -*-

# static 멤버변수 : static영역에 하나만 -> 공통속성
#                    -> 메모리 절약 -> Python이?
#                    -> 없음

# static 메소드 : (메소드 절약이 없지는 않은데)
#                객체 안만들고 쓰는 메소드

# 계산기

class calculator:
    @staticmethod
    def printHab(a, b): # 첫번째 파라메터 self없으면 static메소드
        print(a + b)





calculator.printHab(10, 20)










