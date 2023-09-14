# -*- coding:utf-8 -*-

# 메뉴
# 메뉴명이 김치찌개
# 가격이 9000원
# 정보 출력


class Menu:
    name = None
    price = None
    
    # constructor(생성자)
    #    overloading이 안되니 -> 생성자는 하나만 가능
#     def __init__(self): # Python의 생성자
#         print("메뉴객체 생성됨")
#         print("생성자 전혀 건들지 않으면 자동으로")
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # destructor(소멸자)
    def __del__(self):
        print("메뉴객체 없어짐")
    
    def printInfo(self):
        print(self.name)
        print(self.price)
        
# 멤버 변수 써봐야 의미가 없고(외부에서 넣을수 있으니)
# 메소드는 정해진대로 쓰고     
# Overloading이 안되니 생성자는 하나만 가능하고
# => 생성자에서 멤버변수를 경정하는 경향이...
class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def printInfo(self):
        print(self.name, self.price)
#####################################        
p = product("포크", 1500)
p.printInfo()


m = Menu("김치찌개", 9000)
m.printInfo()




