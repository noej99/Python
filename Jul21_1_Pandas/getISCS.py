# -*- encoding:utf-8 -*-
from http.client import HTTPConnection
from json import loads


# BSSH_NM
# INDUTY_DESC
# ADRES_CN2
# PRDLST_DESC
# PC

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/IndividualServiceChargeService/1/1000
f = open("C:/noej/sourceFile/data/csv/iscs.csv", "a", encoding="utf-8")

huc = HTTPConnection("openapi.seoul.go.kr:8088")
for i in range(1, 7002, 1000):
    huc.request("GET", "/575a4655496b636839386f58586542/json/IndividualServiceChargeService/%d/%d" % (i, i+999))
    resBody = huc.getresponse().read()

    data = loads(resBody)

    for d in data["IndividualServiceChargeService"]["row"]:
        f.write("%s," % d["BSSH_NM"].replace(",", ""))
        f.write("%s," % d["INDUTY_DESC"].replace(",", ""))
        f.write("%s," % d["ADRES_CN2"].replace(",", ""))
        f.write("%s," % d["PRDLST_DESC"].replace(",", ""))
        f.write("%.1f\n" % d["PC"])
huc.close()
f.close()




