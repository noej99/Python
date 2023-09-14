# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/700/201501/

f = open("C:/Users/jny09/0x4E/use/cspf.csv", "a", encoding="utf-8")
# f = open("c:/noej/cspf.csv", "a", encoding="utf-8")

for y in range(2015, 2023):
    for m in range(1, 13):
        t = "%d%02d" % (y, m)
        huc = HTTPConnection("openapi.seoul.go.kr:8088/")
        huc.request("GET", "/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/700/" + t)
        rb = huc.getresponse().read()

    for s in loads(rb)["CardSubwayPayFree"]["row"]:
        f.write("%s," % s["USE_MON"])
        f.write("%s," % s["LINE_NUM"])
        f.write("%s," % s["SUB_STA_NM"].replace(",", "."))
        f.write("%.0f," % s["PAY_RIDE_NUM"])
        f.write("%.0f," % s["FREE_RIDE_NUM"])
        f.write("%.0f," % s["PAY_ALIGHT_NUM"])
        f.write("%.0f\n" % s["FREE_ALIGHT_NUM"])
    print(t)

huc.close()
f.close()