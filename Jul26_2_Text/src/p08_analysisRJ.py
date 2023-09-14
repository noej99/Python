# -*- coding:utf-8 -*-
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

sw = stopwords.words("english") # 불용어 list
wnl = WordNetLemmatizer() # 표제어 추출기

f = open("C:/Users/jny09/OneDrive/바탕 화면/rj.txt", "r", encoding="utf-8")

wc = {}
txt = f.read() # 한번에 다 읽어서 str로
wt = word_tokenize(txt) # 단어별로 뜯어서
wt = pos_tag(wt) # 품사 태그
for w, p in wt:
    w = w.lower() # 소문자로 바꿔서
    if w not in sw: # 불용어에 없는것만
        if p.startswith("V"): # 동사만(품사가 V로 시작하는)
            w = wnl.lemmatize(w, wordnet.VERB) # 원형으로
            if w in wc:
                wc[w] +=1
            else:
                wc[w] =1
f.close()

wcList = []
for k, v in wc.items():
    wcList.append({"단어":k, "횟수":v})

wcDF = pd.DataFrame(wcList)

# 횟수 내림차순 정렬해서 뭔 단어 많이 썼나
wcDF =wcDF.sort_values(by="횟수", ascending=False)
print(wcDF)

# 단어별 횟수 막대그래프
wcDFTOP30 = wcDF.head(30)
sns.barplot(data=wcDF, x="단어", y="횟수", palette="pastel")
plt.show()

# pd.DataFrame -> csv(필드명/인덱스 까지)
# wcDF.to_csv("C:/Users/jny09/OneDrive/바탕 화면/rjWC.csv")

# pd.DataFrame -> csv(필드명/인덱스 빼고)
wcDF.to_csv("C:/Users/jny09/OneDrive/바탕 화면/rjWC.csv", index=False, header=False)
# wcDF.to_csv("C:/noej/sourceFile/data/csv/rjWC.csv", index=False, header=False)

# csv에 쓰기
# f2 = open("C:/noej/sourceFile/data/csv/rjWC.csv", "a", encoding="utf-8")
# f2 = open("C:/Users/jny09/OneDrive/바탕 화면/rjWC.csv", "a", encoding="utf-8")
# for k, v in wc.items():
#     f.write("%s,%d\n" % (k, v))
# f2.close()    


