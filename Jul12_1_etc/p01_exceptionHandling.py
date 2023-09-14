# -*- coding:utf-8 -*-

# error : 문법에 안맞게 써서, 기계어 번역 불가
#        최종 산출물이 안나옴 -> 실행 불가

# warning : 정리안된 소스
#        실행은 가능

# exception : 프로그램은 문제없이 완성
#        실행때 뭔가 잘못되어서 정상 진행이 안되는 상황

# error vs exception?

# Python은 interpreter방식이라서 error/exception구별이 안됨
#    문법에 안맞 : error
#    실행때 터진 : exception

# .jar 소스못보고/수정못하게

# J : 예외처리 필수
#        try-catch-finally(직접처리), throws(처리를 호출한 쪽에서)
# P : 예외처리 필수 아님
#        try-except-else-finally
# try:
#     x = int(input("x : "))
#     y = int(input("y : "))
#     z = x / y
#     print(z)
#     
#     l = [10, 20, 30]
#     print(l[y])
#     
# except ZeroDivisionError:
#     print("나누기 0?")
#     
# except IndexError:
#     print("리스트에 없습니다")

# except에 에러내용 안적으면 다 받음

try:
    x = int(input("x : "))
    y = int(input("y : "))
    z = x / y
    print(z)
     
    l = [10, 20, 30]
    print(l[y])
except Exception as e:
    print(e) # e.printstacktrace()
else:
    print("문제없으면")
finally:
    print("문제가 있든 없든 리턴보다 먼저")
    
    
    
    
    
    
    
    