# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/1000/20150101/
y = input("년 : ")
huc = HTTPConnection("openapi.seoul.go.kr:8088")
for m in range(1, 13):
    for d in range(1, 32):
        for i in range(1, 41000, 1000):
            t = "/%d/%d/%s%02d%02d" % (i, i+999, y, m, d)
            print(t)
            huc.request("GET", "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew" + t)
            resBody = huc.getresponse().read()
            f = open("C:/noej/sourceFile/data/csv/bus%s.csv" % y, "a", encoding="utf-8")
            bus = loads(resBody)
            if "CardBusStatisticsServiceNew" in bus:
                # "CardBusStatisticsServiceNew"안에 있으면
                for b in bus["CardBusStatisticsServiceNew"]["row"]:
                    s = b["USE_DT"]
                    date = ("%s,%s,%s," % (s[0:4], s[4:6], s[6:8]))
                    br = b["BUS_ROUTE_NM"]
                    bs = b["BUS_STA_NM"]
                    rpn = int(b["RIDE_PASGR_NUM"])
                    apn = int(b["ALIGHT_PASGR_NUM"])
                    f.write("%s%s,%s,%d,%d\n" % (date, br, bs, rpn, apn))
        print(y, m, d)
huc.close()
f.close()