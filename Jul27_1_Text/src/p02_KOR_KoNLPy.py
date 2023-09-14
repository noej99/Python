# -*- coding:utf-8 -*-
from konlpy.tag._okt import Okt

# NLTK : 한글은 약하고
# KoNLPy
#    Java로 만들어져 있어서 -> 컴에 Java가 있어야
#    Java를 활용하는 Python프로그램 돌리려면 : jpype
#        pip install jpype1
#    pip install konlpy
t = "몽둥이 금지라구요??? 당연한 말씀 그럼 방망이? 몽둥이, 회초리, 공포의 쓴맛?!"
t += "집에 가고싶어요 저런... 쌤 저 롤스로이스 고스트 사주세요 네? 안된다구요... 네..."

o = Okt()   # Open Korean Text 분석기
            # (구] 트위터 한글 형태소 분석기)
tt = "안녕하세욬ㅋㅋㅋㅋㅋ"
a = o.normalize(tt) # 정규화(정리)
print(a)
print("-----")

b = o.phrases(t) # 어구 추출(의미있는 단위로 나누기))
print(b)
print("-----")

c = o.morphs(t) # 형태소 분석
print(c)
print("-----")

d = o.morphs(t, stem=True) # 형태소 분석(기본형으로)
print(d)
print("-----")

e = o.pos(t)    # 형태소 분석(품사 태그) ->
                # (단어, 품사)의 tuple list
for w, p in e:
    print(w, p)
print("-----")

f = o.pos(t, join=True) # 형태소 분석(품사 태그)
                        # 단어/품사의 str list
for wp in f:
    print(wp)
print("-----")

g = o.pos(t, stem=True) # 형태소 분석(춤사 태그, 기본형으로)
for w, p in g:
    print(w, p)
print("-----")

h = o.nouns(t) # 명사만
for w in h:
    print(w)