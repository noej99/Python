# -*- coding:utf-8 -*-
from Human import Human

class Avengers:
    # python은 멤버 변수 따로 쓰는게 별 의미가 없고
    # python은 오버로딩 없고 -> 생성자가 하나밖에 안됨
    # -> 보통 생성자에서 멤버변수를 결정
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def attack(self):
        print("공격")
        
    def show(self):
        print(self.name, self.age)

########################

# p : 생성자 상속됨
# overriding : 물려받은 메소드 재정의
# overloading : 함수명 같게, 파라메터 다르게

# OOP : 상속(상위클래스 기능 물려받고, 기능 추가)
# 어벤져스
#    이름, 나이
#    공격하기
#    정보출력
# 아이언맨
#    비서컴
class Ironman(Avengers):
    # overriding? or overloading?
    # 결국 새로만든... -> 자바가 생성자 상속을 안시킨 이유
    def __init__(self, name, age, ai):
        super().__init__(name, age)
        # Avengers.__init__(self, name, age)
        self.ai = ai
     
    # overriding    
    def show(self):
        Avengers.show(self)
        print(self.ai)
########################

# 배너, 25, 바지사이즈가 40인 헐크
# 공격
# 정보출력
class Herk(Avengers):
    
    def __init__(self, n, a, p):
        super().__init__(n, a)
        self.pantsSize = p
        
    def show(self):
        Avengers.show(self)
        print(self.pantsSize)
########################

# J : 다중상속 x
# P : 다중상속
#    Avengers/Human 메소드명 같으면?
#    먼저 상속받은걸로 쳐줌
#    다중 상속...?
class Spiderman(Avengers, Human):
    pass
# 생성자가 상속됨
#    Avengers - 이름, 나이
#    Human - 집 주소
########################
# 다중상속 받았다 -> 이름, 나이, 집주소
class CaptainAmerica(Avengers, Human):
    def __init__(self, n, a, h):
        Avengers.__init__(self, n, a)
        Human.__init__(self, h)
    
    def show(self):
        Avengers.show(self)
        Human.show(self)
########################
i = Ironman("토니", 30, "자비스")
i.attack()
i.show()
print("-----")
h = Herk("배너", 25, 40)
h.attack()
h.show()
print("-----")
s = Spiderman("톰", 19)
s.attack()
s.eat()
s.show()
print("-----")
c = CaptainAmerica("캡", 75, "서울")
c.show()
print("-----")



