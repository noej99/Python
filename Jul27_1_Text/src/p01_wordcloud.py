# -*- coding:utf-8 -*-

# pip install wordcloud==1.8.0

from wordcloud.wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# matplotlib에 글자 한글
FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

f = open("C:/Users/jny09/OneDrive/바탕 화면/Sam10.txt", "r", encoding="utf-8")

# 단어 수 세어놓을 필요 없고, 띄어쓰기 기준으로 단어가 띄어져있기만하면 알아서

txt = f.read()

wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color="white").generate(txt) # 워드클라우드 이미지
plt.imshow(wc) # 이미지그리기
plt.show()

f.close()