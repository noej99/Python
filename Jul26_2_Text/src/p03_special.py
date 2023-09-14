# -*- coding:utf-8 -*-
from sys import maxunicode
from unicodedata import category
from test.test_long import special

# unicode : 컴퓨터상에 문자 표현하는 방식
# UnicodeTransfFomat-8bit

print(maxunicode) # 전체 unicode문자 수
print(chr(1030)) # 1030번째 unicode문자
print(category('!')) # 뭐
# unicode category로 검색해서...
print("------")

for i in range(maxunicode):
    # print(chr(i)) 
    # print(category(chr(i)))
    if category(chr(i)).startswith("P"):
        special.append(chr(i))
print(special)
print("----")

# 삼국지10권
f = open("C:/Users/jny09/OneDrive/바탕 화면/Sam10.txt", "r", encoding="utf-8")
wordCountDict = {}
for line in f.readlines():
    line = line.replace("\n", "")
    for word in line.split(" "):
        for s in special:
            word = word.replace(s, "")
        
        if word in wordCountDict:
            wordCountDict[word] += 1
        else:
            wordCountDict[word] = 1
f.close()

for k, v in wordCountDict.items():
    print(k, v)