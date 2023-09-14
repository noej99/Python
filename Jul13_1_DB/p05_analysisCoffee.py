# -*- coding:utf-8 -*-

class Coffee:
    def __init__(self, l):
        l = l.split(",")
        self.name = l[0]
        self.cate = l[1]
        self.price = int(l[2])

    def show(self):
        print(self.name, self.cate, self.price)
#####################################################################
f = open("C:/noej/sourceFile/coffeeTest.csv", "r", encoding="utf-8")

coffees = [] # ArrayList<Coffee>
for l in f.readlines():
    print(l.replace("\n", ""))
    c = Coffee(l)
    coffees.append(c)
    
f.close()
#####################################################################
# 1) 평균가
hab = 0
for c in coffees:  # for (Coffee c : coffees)
    hab += c.price # c.getPrice()
print(hab / len(coffees))
print("-------")

# 2) 메뉴 총 몇 종류
print(len(coffees))
print("-------")

# 3) 최고가 메뉴 ?/ 최저가 메뉴 ?
coffees.sort(key=(lambda cf:cf.price), reverse=True)
print(coffees[0].show())
print(coffees[-1].show())
