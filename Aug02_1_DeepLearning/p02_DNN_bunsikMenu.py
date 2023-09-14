# -*- coding:utf-8 -*-
import cv2
import os
import tensorflow as tf

def getImg(folder, w, h):
    imgs = []
    files = os.listdir(folder) # 그 폴더에 있는 파일명들
    for f in files:
        i = cv2.imread(folder + "/" + f, cv2.IMREAD_GRAYSCALE)
        i = cv2.resize(i, (w, h))
        i = i.flatten()
        imgs.append(i)
    return imgs

xData = getImg("C:/noej/sourceFile/zawon/bunsikMenu", 100, 50)
# tf에 one-hot encoding해주는 메소드가 있어서
# yData = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], ...]
yData = [0,0,0,0,0, 1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4] # label인덱스
label = ["떡볶이", "오뎅", "김밥", "튀김", "순대"]

x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

# 1x2 -> 1x5000
a1 = tf.Variable(tf.random_uniform([len(xData[0]), 1000], -10, 10, tf.float64))
b1 = tf.Variable(tf.random_uniform([1000], -10, 10, tf.float64))
sik1 = tf.add(tf.matmul(x, a1), b1)
sik1 = tf.nn.relu(sik1)

# [100, 20, 30, 0, 0] -> [10, 30, -5, -4] -> [10, 30, 0, 0]
a2 = tf.Variable(tf.random_uniform([1000, 1000], -10, 10, tf.float64))
b2 = tf.Variable(tf.random_uniform([1000], -10, 10, tf.float64))
sik2 = tf.add(tf.matmul(sik1, a2), b2)
sik2 = tf.nn.relu(sik2)

# [10, 30, 0, 0] -> [-3, -10, 100, 30, 1] -> [0, 0, 100, 30, 1]
a3 = tf.Variable(tf.random_uniform([1000, 1000], -10, 10, tf.float64))
b3 = tf.Variable(tf.random_uniform([1000], -10, 10, tf.float64))
sik3 = tf.add(tf.matmul(sik2, a3), b3)
sik3 = tf.nn.relu(sik3)

# [0, 0, 100, 30, 1] -> [1, 0]
# 다음층이 없으니 어차피 더 이상 계산 없음
# 최종 결과낼때 최대값이 있는 인덱스를 찾고
# => 활성화 함수 필요없을 것
a4 = tf.Variable(tf.random_uniform([1000, len(label)], -10, 10, tf.float64))
b4 = tf.Variable(tf.random_uniform([len(label)], -10, 10, tf.float64))
sik4 = tf.add(tf.matmul(sik3, a4), b4)

# 실제 y, sik을 통해서 구해진거 거리
d = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=sik4))

ao = tf.train.AdamOptimizer(learning_rate=0.00001)
goal = ao.minimize(d)
################################################################
s = tf.Session()
s.run(tf.global_variables_initializer())

yData = s.run(tf.one_hot(yData, len(label)))
print(yData)

while True:
    s.run(goal, {x:xData, y:yData})
    dd = s.run(d, {x:xData, y:yData})
    print(dd)
    print("-----")
    
    if dd < 0.01:
        break
    
while True:
    ff = input("경로 : ")
    ff = cv2.imread(ff, cv2.IMREAD_GRAYSCALE)
    ff = cv2.resize(ff, (100, 50))
    ff = [ff.flatten()]
    result = s.run(tf.argmax(sik4, 1), {x:ff})[0]
    print(label[result])

# canvas로 그린거 저장이 되니    
# JSP/Spring의 파일업로드
# DNN + FlaskWAS

