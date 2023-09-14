# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/ListNecessariesPricesService/1/1000/
# m_name, a_name, a_price, m_type_name, m_gu_name
huc = HTTPConnection("openapi.seoul.go.kr:8088")
for i in range(1, 558632, 1000):
    n = "%d/%d/" % (i, i+999)
    huc.request("GET", "/575a4655496b636839386f58586542/json/ListNecessariesPricesService/" + n)
    resBody = huc.getresponse().read()
    data = loads(resBody)

    f = open("C:/noej/sourceFile/data/csv/lnps.csv", "a", encoding="utf-8")

    for d in data["ListNecessariesPricesService"]["row"]:
        f.write("%s," % d["M_NAME"].replace(",", "."))
        f.write("%s," % d["A_NAME"].replace(",", "."))
        f.write("%s," % d["A_PRICE"])
        f.write("%s," % d["M_TYPE_NAME"].replace(",", "."))
        f.write("%s\n" % d["M_GU_NAME"].replace(",", "."))
    print(n)
huc.close()
f.close()
