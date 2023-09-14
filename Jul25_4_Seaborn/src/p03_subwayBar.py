# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

# 지하철csv불러서
subwayDF = pd.read_csv("C:/noej/sourceFile/data/csv/subway.csv", names=["년", "월", "일", "이용객수", "타", "내리"])
subwayDF["이용객수"] = subwayDF["타"] + subwayDF["내리"]

def getYoil(s):
    date = "%d%02d%02d" % (s["년"], s["월"], s["일"])
    date = datetime.strptime(date, "%Y%m%d")
    return datetime.strftime(date, "%a")
    
subwayDF["요일"] = subwayDF.apply(getYoil, axis=1)
print(subwayDF)

# 노선별 이용객수 평균(요일별로 따로)
sns.barplot(x="노선", y="이용객수", hue="요일",  data=subwayDF)

# 요일별 이용객수 평균
# sns.barplot(x="요일", y="이용객수", data=subwayDF)

# def test(t):
#     print(t["년"])
#     print(t["월"])
#     print(t["일"])
#     print("-----")

# subwayDF["년"].apply(test)
# subwayDF.apply(test, axis=1)

#노선별 이용객수 평균
# sns.barplot(x="노선", y="이용객수", data=subwayDF)

# 노선별 데이터 수
# sns.countplot(x="노선", data=subwayDF)

plt.show()