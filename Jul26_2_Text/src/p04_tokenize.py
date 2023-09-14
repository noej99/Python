# -*- coding:utf-8 -*-
from nltk.tokenize import word_tokenize, sent_tokenize

# pip install nltk
# NLTK(Natural Language ToolKit) : 한글은 부실

t = "몽둥이 금지라구요??? 당연한 말씀 그럼 방망이? 몽둥이, 회초리, 공포의 쓴맛?!"
t += "집에 가고싶어요 저런... 쌤 저 롤스로이스 고스트 사주세요 네? 안된다구요... 네..."

# 특수문자 목록 다운받기(처음 한번만)
# import nltk
# nltk.download("punkt")
wt = word_tokenize(t) # 단어 분리(특수문자까지)
print(wt) 

st = sent_tokenize(t) # 문장 분리
print(st)
