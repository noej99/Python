# -*- coding:utf-8 -*-
# Numpy/Pandas -> SQL
# Matplotlib/Seaborn -> canvasjs

# pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# matplotlib이 쓰는 기본폰트가 한글이 없어서
# 헌글이 되는 폰트로 바꿔야
# C:\Windows\fonts에 가서 cmd -> dir로 확인
# 안되는폰트도 존재
FontFile = "C:/Windows/Fonts/malgun.ttf" # 폰트파일 경로
fontName = fm.FontProperties(fname=FontFile, size=10).get_name() # 폰트이름
plt.rc("font", family=fontName) # 앞으로 그래프 그릴때 저 폰트 사용

# numpy array를 대상
xData = np.array([10, 20, 30, 40, 50])
yData = [10, 32, 1, 5, 23] # list -> numpy array로 자동으로 바꿔서

# 기본
# plt.plot(yData)
# plt.show()

# x, y
# plt.plot(xData, yData)
# plt.show()


# 축
# plt.plot(xData, yData)
# plt.xlabel("x축 제목") 
# plt.ylabel("y축 제목") 
# plt.axis(0, 100, 1, 200) # x시작, x끝, y시작, y끝
# plt.show()

# 제목
# plt.plot(xData, yData)
## plt.title("제목")
# plt.title("제목", loc="left") # left, center, right
# plt.title("ㅋㅋㅋ", loc="right") # 여러개 가능
# d = {"fontsize":20, "fontweight":"bold","color":"red"}
# plt.title("ㅎ", loc="center", fontdict=d)
# plt.show()

# 선(간단하게)
# matplotlib cheatsheet
# plt.plot(xData, yData, "m:P") # 색, 선, 마커
# plt.show()

# 그리드
# plt.plot(xData, yData)
# plt.grid(axis="y", color="red", linestyle=":")
# plt.grid(axis="x")
# plt.show()

# 눈금
# plt.plot(xData, yData)
plt.xticks(xData, ["십", "이십", "삼십", "사십", "오십"])
# 데이터에 맞추자면
# plt.yticks(yData, ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"])
# yData = [10,   32, 1, 5, 23]
#         ["ㄱ", "ㄴ", ...]
# 10에 ㄱ, 32에 ㄴ

# 균등하게 하자면
# plt.yticks([0, 10, 20, 30], ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"])
plt.yticks(np.arange(0, 31, 10), ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"])
# 눈금     x, y both   in, out, inout    눈금-글자 간격
plt.tick_params("y", direction="in", length=15, pad=30)
# 글자
# plt.tick_params("x", labelsize=30, labelcolor="#0000FF")
# plt.show()

# 선 여러개
yData2 = [100, 300, 10, 500, 30]
plt.plot(xData, yData, color="red")
plt.plot(xData, yData2, color="green")
plt.legend("빨강", "녹색")
plt.show()

# 전체, 첫번째 x축 설정 = plt.subplots()
_, sub1conf = plt.subplots()
p1 = sub1conf.plot(xData, yData, COLOR="red")
sub1conf.set_xlabel("엑스")
sub1conf.set_ylabel("와이1")
# 첫번째 x축 설정 복사
sub2conf = sub1conf.twinx()
p2 = sub2conf.plot(xData, yData2, color="green")
sub2conf.set_ylabel("와이2")
# 범례
sub1conf.legend(p1+p2, ["빨", "녹"])
plt.show()
