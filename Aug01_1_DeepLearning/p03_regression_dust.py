# -*- coding:utf-8 -*-
import tensorflow as tf
from http.client import HTTPConnection
from json import loads
import pandas as pd
# 서울시 실시간 미세먼지
# 미세먼지가 30이면 -> 초미세먼지는 얼마?

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25")
rb = huc.getresponse().read()
df = pd.DataFrame(loads(rb)["RealtimeCityAir"]["row"])
huc.close()
xData = df["PM10"]
yData = df["PM25"]
################################################################
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)
a = tf.Variable(tf.random_uniform([1], -10, 10, tf.float64))
b = tf.Variable(tf.random_uniform([1], -10, 10, tf.float64))
sik = a * x + b
d = tf.reduce_mean(tf.square(y - sik))
ao = tf.train.AdamOptimizer(learning_rate=0.0001)
goal = ao.minimize(d)
################################################################
s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    print("y = %fx + %f" % (s.run(a), s.run(b)))
    dd = s.run(d, {x:xData, y:yData})
    print(dd)
    print("-----")
    
    if dd < 10:
        break
################################################################
# 3) 예측
newX = float(input("PM10 : "))
result = s.run(sik, {x:newX})[0]
print(result)


