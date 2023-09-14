# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

yData = [10, 30, 5, 32, 1]
xData = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"]

# 기본
# plt.bar(xData, yData)
# plt.show()

# 디자인
# plt.bar(xData, yData, color="orange", width=0.5, edgecolor="red", linewidth=3)
cs = ["red", "orange", "yellow", "green", "blue"]
plt.bar(xData, yData, color=cs, width=0.5, edgecolor="red", linewidth=3)
plt.show()

# 여러개
yData2 = [12, 33, 53, 1, 23]
xData2 = np.arange(len(yData2)) # 0 1 2 3 4
xData3 = xData2 - 0.4 # -0.4 0.6 ...
# plt.bar(xData, yData, align="edge")

# -0.4 0.6 ...
plt.bar(xData3, yData, width=0.4, align="edge")
# 0 1 ...
plt.bar(xData, yData2, width=0.4, align="edge", color="green")
plt.show()

# 여러개(위에 - 누적합)
yData2 = [12, 33, 53, 1, 23]
plt.bar(xData, yData, color="red")
plt.bar(xData, yData2, color="blue", bottom=yData)
plt.show()





