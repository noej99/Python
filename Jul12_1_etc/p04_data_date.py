# -*- coding:utf-8 -*-

# J
#   Date : 2000년대를 생각하지 않던 시절에 만들어져서
#       deprecated
#   SimpleDateFormat : Date활용을 서포트(Date <-> String)

# P
#   datetime : 2000년대를 반영해서 만들어져있음

# 패키지 없음
from datetime import datetime
from time import strftime
    # datetime.py    # class datetime

now = datetime.today()  # static메소드
print(now)

# J
#    캡슐화 -> now.getYear(); : 2000년대...
# P
#    접근제어자 없 -> 캡슐화 없
print(now.year) # 연도
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print("-------------")
# 특정시간날짜
d = datetime(2222,2,22,2,22,22)
print(d)

d2 = input("아무 날짜(YYYY/MM/DD) : ")
# 입력받은거를 datetime객체로
d2 = datetime.strptime(d2, "%Y/%m/%d")
print(d2)
d2 = datetime.strftime(d2, "%m%d")
print(d2)
# d2 = d2.split("/")
# d2 = datetime(int(d2[0]),int(d2[1]),int(d2[2]))
# print(d2)
# J의 SimpleDateFormat같은거

# str -> datetime
# datetime.strptime(datetime객체, "패턴")

# datetime -> str
# datetime.strftime(str객체, "패턴")

# 패턴 확인
# help(strftime)
print("-------")
bd = input("생일(YYYY/MM/DD) : ")
bd = datetime.strptime(bd, "%Y/%m/%d")
print(datetime.strftime(bd, "%A"))
age = (datetime.today().year - bd.year + 1) 
print(age)
