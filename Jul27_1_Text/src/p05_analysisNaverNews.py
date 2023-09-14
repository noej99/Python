# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from hanspell.spell_checker import check
from konlpy.tag._okt import Okt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

# MongoDB에 있는 네이버 뉴스 다
con = MongoClient("195.168.9.61")
db = con.xe
o = Okt()
wc ={}
for n in db.naverNews.find():
    n = n["title"] + " "  + n["desc"]
    n = check(n).checked # 맞춤법 교정
    n = o.normalize(n) # 정규화
    for w, p in o.pos(n, stem=True): # 형태소 분석(동사 원형으로)
        if p == "Verb": # 동사만
            if w in wc:
                wc[w] += 1
            else:
                wc[w] = 1
wc2 = []
for w, c in wc.items():
    wc2.append({"단어":w, "횟수":c})

# 가나다순 정렬해서
wcDF = pd.dataframe[wc2]
wcDF= wcDF.sort_values(by="단어")
print(wcDF)

# 막대그래프
sns.barplot(x="단어", y="횟수")
plt.show()

con.close()

