# -*- coding:utf-8 -*-

class CPU:
    name = None
    price = None
    
    def __init__(self):
        print("cpu생성")
        
    def __del__(self):
        print("cpu사라짐")
    
    def printInfo(self):
        print(self.name, self.price)

######################################

c = CPU()
c.name = "i7-13200"
c.price = 780000
c.printInfo()

c2 = CPU()
c2.name = "i9-14400"
c2.price = 1080000
CPU.printInfo(c2)

c3 = c
c3.name = "i3-9800"
c3.printInfo()

c.printInfo()

c = None
c3 = None
c2 = None
print("ㅋㅋㅋㅋㅋ")

#    static/stack : 프로그램 종료되면 메모리 정리
#    heap : 메모리는 수동으로 정리해야

# Garbage Collection 
#    heap영역 자동정리 시스템
#    그 자동이 언제 : 그 주소 더이상 못쓰게 되면
#    Java/Python개발자는 메모리 관리 몰라도
#    BD/AI에서는...



