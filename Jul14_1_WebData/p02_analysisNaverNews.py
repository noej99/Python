# -*- coding:utf-8 -*-

f = open("C:/noej/sourceFile/data/csv/naverNews.txt", "r", encoding="utf-8")
wcDict = {} # str -> int
for l in f.readlines():
    l = l.replace("\n", "").split("\t")
    for word in l[1].replace("[", "").replace("]", "").split(" "):
        if word in wcDict:
            # 단어가 dict에 있으면 +1
            wcDict[word] += 1
        else:
            # 단어가 dict에 없으면 1
            wcDict[word] = 1
            
# for문 문법이
# for 변수 in 컬렉션:
for k, v in wcDict.items():
    print(k, v)
f.close()