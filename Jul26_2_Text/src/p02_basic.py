# -*- coding:utf-8 -*-

# 무슨 단어가 몇번 나오나
# f = open("C:/noej/sourceFile/data/csv/sam10.txt", "r", encoding="utf-8")
f = open("C:/Users/jny09/OneDrive/바탕 화면/Sam10.txt", "r", encoding="utf-8")
wordCountDict = {}
for line in f.readlines():
    line = line.replace("\n", "")
    for word in line.split(" "):
        if word in wordCountDict:
            wordCountDict[word] += 1
        else:
            wordCountDict[word] = 1
f.close()

import pandas as pd

wordCountDF = pd.DataFrame(wordCountDict)
print(wordCountDF)

# for k, v in wordCountDict.items():
#     print(k, v)