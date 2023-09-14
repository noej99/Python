# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/1000/20230710

# 정형 -> OracleDB
# 실시간이 아니기에 굳이 DB에 저장할 이유가 없어서
# 바로 csv파일로

# 1) HTTP통신여부
# 2) 파싱
huc = HTTPConnection("openapi.seoul.go.kr:8088")
for y in range(2015, 2023):
    for m in range(1, 13):
        for d in range(1, 32):
            when = "%d%02d%02d" % (y, m, d)
            print(when)
            huc.request("GET", "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/700/" + when)
            resBody = huc.getresponse().read()

            f = open("C:/noej/sourceFile/data/csv/subway.csv", "a", encoding="utf-8")

            for s in fromstring(resBody).getiterator("row"):
                if s == None:
                    break
                d = s.find("USE_DT").text
                f.write("%s,%s,%s," % (d[0:4], d[4:6], d[6:8]))
                f.write("%s," % s.find("LINE_NUM").text)
                f.write("%s," % s.find("SUB_STA_NM").text)
                f.write("%s," % s.find("RIDE_PASGR_NUM").text)
                f.write("%s\n" % s.find("ALIGHT_PASGR_NUM").text)
            print(when)

huc.close()

f.close()