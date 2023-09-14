# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

import pandas as pd

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = huc.getresponse().read()

data = loads(resBody) # JSON -> Python dict + list
dustDF = pd.DataFrame(data["RealtimeCityAir"]["row"])
print(dustDF)

huc.close()
