# -*- coding:utf-8 -*-

score = int(input("시험점수 : "))

# 파이썬 if문에서 ()생략 가능

if score > 80:
    print("잘했다")
elif score > 60:
    print("그렇구나")
elif score > 50:
    print("그..렇구나")
elif score > 40:
    print("그.....렇구나")
else:
    print("...")

# 3항연산, switch-case문
# if문으로 해도 됨, 소스가 길어지지만...
# -> 파이썬에서는 없음