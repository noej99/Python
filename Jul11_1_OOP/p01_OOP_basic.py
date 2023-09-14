# -*- coding:utf-8 -*-

# J : Perfect OOP
#    package(필수) > class(필수)
# p : Hybrid OOP -> 객체지향 안하려면 안하는거
#        1 file = 1 module
#    package(안해도) > module(필수) > class(안해도)

# OOP
#   1 file = 1 class -> 코드 재사용

# 클래스명을 대문자로 시작 : Java진영

# 클래스명 대문자로 시작 안해도됨
# 접근제어자 없음 -> 캡슐화 없음, 패턴프로그래밍 없음

class dog:
    name = None
    age = None
    
    def bark(self): # 메소드는 첫번째 파라메터로 self
        print("멍")
        
    def printInfo(self):
        print(self.name)    
        print(self.age)    
        print(self.type)    
#################

# 하지만 소문자로 하면 객체만드는건지 함수불러오는건지 구분이 안됨
d = dog() 
d.name = "후추"
d.age = 3
d.type = "푸들" # 클래스 외부에서 멤버변수 추가 가능
# Python스타일(클래스명.xxx(객체))
dog.bark(d)
dog.printInfo(d)

# 대부분 PL들의 스타일(객체.xxx)
d.bark() # 메소드 호출때는 self는 없는 취급
d.printInfo()



