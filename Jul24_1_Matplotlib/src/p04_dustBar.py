# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

# 서울 실시간 미세먼지
# 구별로 미세+초미세 막대그래프
huc = HTTPConnection("openapi.seoul.go.kr:8888")
huc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
rb = huc.getresponse().read()
huc.close()

dustData = loads(rb)
dustData = dustData["RealtimeCityAir"]["row"]
dustDF = pd.DataFrame(dustData)

gu = dustDF["MSRSTE_NM"]
pm10 = dustDF["PM10"]
pm25 = dustDF["PM25"]

plt.bar(gu, pm10, color="red")
plt.bar(gu, pm25, color="blue", bottom=pm10)
plt.title("미세먼지")
plt.show()






