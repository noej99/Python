# -*- coding:utf-8 -*-

from hanspell.spell_checker import check
from konlpy.tag._okt import Okt
import seaborn as sns
from wordcloud.wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from p05_analysisNaverNews import wcDF
import pandas as pd

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

f = open("C:/noej/sourceFile/data/csv/sh3Rsult.txt", "r", encoding="utf-8")
o = Okt()
wc={}
words = ""
for l in f.readlines():
    l = l.split("\t")[0].replace("\"", "")
    l = check(l).checked
    l = o.normalize(l)
    for w, p in o.pos(l, stem=True):
        if p == "Verb":
            wc[w] += 1
        else:
            wc[w] = 1
        words += w + " "
f.close()

f2 = open("C:/noej/sourceFile/data/csv/sh3Rsult2.csv", "a", encoding="utf-8")
for k, v in wc.items():
    f2.write("%s,%d\n" % (k, v))
f2.close()


# wcList = []
# for k, v in wc.items():
#     wcList.append({"단어":k, "횟수":v})
# wcDF = pd.dataframe(wcList)
# wcDF = wcDF.sort_values(by="횟수")
# print(wcDF)

# 막대 그래프
# sns.barplot(x="단어", y="횟수", data=wcDF)
# plt.show()

# 워드 클라우드
wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color="white").generate(words)
plt.imshow(wc)
plt.show()
