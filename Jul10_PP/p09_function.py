# -*- coding:utf-8 -*-

# 1) 함수정의
# def 함수명(변수명=기본값, 변수명=기본값, ...):
#    내용
#    return 값

def yaDambae():
    print("슈퍼가서")
    print("한라산 사와")
    
def test():
    print("ㅋ")

#    : 뒤에 무조건 들여쓰기 들어가야
def test2():
    pass # 들여쓰기 자리 차지

def printHab(x=1, y=2):
    print(x)
    print(y)
    print(x + y)

def funcTest(a=10,b=20,c=30):
    print(a, b, c)

# 함수 overloading : 함수명 같게, 파라메터 다르게
# 함수 기본값/자료형 안쓰고 -> overloading없음
# 정수 2개 넣으면 더 큰 숫자 출력하는 함수
def printBigger(x, y):
    if (x > y):
        print(x)
    else:
        print(y) 

# 정수 2개 넣으면 계산하는
def calculate(x, y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a, b, c, d
    # 함수 하나에서 리턴 여러개가 아닌 tuple의 특성 활용
    
# 문장 하나 넣으면, 첫번째글자/마지막글자 구하는
def getFL(txt):
    return txt[0], txt[-1]  # 사실은 tuple하나 -> 리턴 여러개같이 생김

############################    
# 2) 함수호출
# 함수명(값, 값, ...)
# 함수명(변수명=값, 변수명=값, ...)
yaDambae()
test()
printHab(10, 20)
printHab(y=100, x=50)
printHab()
printHab(y=10)
funcTest()
funcTest(b=200, c=300, a=100)
funcTest(1000, c=3000)
printBigger(100, 20)
# aa = calculate(30, 50)
# print(aa, type(aa))
(aa, bb, cc, dd) = calculate(30, 50)
print(aa)
print(bb)
print(cc)
print(dd)
fl = getFL("가나다라마바사아자차카타파하")
print(fl, type(fl))

f, _ = getFL("아야어여오요우유으이")  # 변수를 생성하거나 받기 싫으면 _로 흘려보내기
print(f)
