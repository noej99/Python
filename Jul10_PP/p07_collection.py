# -*- coding:utf-8 -*-

# [], List, Set, Map
s = "호의가 계속되면 둘리인줄 알아요"
print(s[0])
print(s[-1])
print(s[0:5:2])
print("---------------")

# List
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(a))
print(a)
print(a[0])
print(a[0:3]) # 0 ~ (3 - 1)까지
print(a[0:6:2]) # 0 ~ (6 - 1)까지 2칸씩
print(a[-1]) # 뒤에서 1번
print("---------------")

a.append(10) # 추가
a.insert(11, 112) # 11번자리에 집어넣기
a[0] = 0 # 수정
del a[11] # 삭제
print(len(a)) # 개수

# a.sort()    오름차순
a.sort(reverse=True)    # 내림차순

print(a)
print("---------------")

# set : 순서가 제멋대로, 중복x
#    -> 중복제거용으로 사용
b = {11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 33}
print(b)
print(type(b))

c = [123, 123, 789, 456, 852, 741, 963]
c = set(c)
c = list(c)
c.sort()
print(c)
print("---------------")

# Map = dict
d = {"탄수화물":50, "단백질":30}
print(d)
print(type(d))
print(d["단백질"])
print(d.keys()) # 키 값만 빼줌
print("지방" in d) # 키가 있나
print("단백질" in d)

# Java의 List, Map
# Python의 list, dict

# Python의 list : [1, 2, 3] : JavaScript의 배열
# Python의 dict : {키:값, 키:값} : JS의 객체
# Python의 list + dict : JS의 JSON







