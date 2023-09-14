# -*- coding:utf-8 -*-
from jamo.jamo import h2j, j2hcj
from unicode import join_jamos

# pip install jamo(초성/중성/종성 분리)

# 영어 : a가 한글자
# 한글 : ㄱ ㅏ ㄱ(초성, 중성, 종성)이 합쳐져서 한글자

w = "똥"
print(w.find("ㄸ"))
print("-----")

a = h2j(w) # 조합형 상태로 분리(초성용 ㄸ/중성용 ㅗ/종성용 ㅇ)
print(a)
print(a.find("ㄸ"))
print(a.find("ᄄ"))
print("-----")

b = j2hcj(a) # 조합형 -> 원형
print(b)
print(b.find("ㄸ"))
print("-----")

# hangul-utils github에서 다 필요하지는 않고
# unicode.py만 갖져와서
# 초성/중성/종성 합치기
w2 = "ㅎㅡㅇ"
c = join_jamos(w2)
print(c)

