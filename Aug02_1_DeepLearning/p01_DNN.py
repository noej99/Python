# -*- coding:utf-8 -*-
import tensorflow as tf

# ANN(Artificial Neural Network)
#    [80, 20] -> [1, 0] : 다차원 회귀분석
#    세상 모든일이 식 하나로?? -> 정확도 떨어질 것
#    구간별로 나눠서 식 여러개로
#    근데 컴퓨터가 안따라줬으니...

# DNN(Deep NN)
#    구간별로 나눠서 -> 다차원/다층 회귀분석
#    input layer(입력층) 1
#    hidden layer(은닉층) n
#    output layer(출력층) 1

# CNN(Convolutional NN)
#    차원수를 줄여서(평균을 내든지)
#    [80, 20]을 [50]으로 차원수 줄여서 NN에 넣는
#    빨라짐, 정확도 떨어짐

# RNN(Recurrent NN)
#    NN의 결과를 다시 NN에 넣어서
xData = [[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]]
yData = [[1, 0], [1, 0], [0, 1], [1, 0], [0, 1]]
label = ["액션", "조폭"]

################################################################
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

# 활성화 함수 : 결과에 거의 영향을 못 줄 정도로 작은 값 없애주는 함수
# 전기의 흐름을 묘사하는 중
# 값이 너무 작은거는 생략해버리면
#    (전기가 거의 안흐른거는 아예 안흐른걸로 취급)
# 다음 층 계산할때 빨라질 것

# [80, 20] -> [100, 20, 30, -31, -50] -> [100, 20, 30, 0, 0]
a1 = tf.Variable(tf.random_uniform([len(xData[0]), 100], -10, 10, tf.float64))
b1 = tf.Variable(tf.random_uniform([100], -10, 10, tf.float64))
sik1 = tf.add(tf.matmul(x, a1), b1)
sik1 = tf.nn.relu(sik1)

# [100, 20, 30, 0, 0] -> [10, 30, -5, -4] -> [10, 30, 0, 0]
a2 = tf.Variable(tf.random_uniform([100, 1000], -10, 10, tf.float64))
b2 = tf.Variable(tf.random_uniform([1000], -10, 10, tf.float64))
sik2 = tf.add(tf.matmul(sik1, a2), b2)
sik2 = tf.nn.relu(sik2)

# [10, 30, 0, 0] -> [-3, -10, 100, 30, 1] -> [0, 0, 100, 30, 1]
a3 = tf.Variable(tf.random_uniform([1000, 500], -10, 10, tf.float64))
b3 = tf.Variable(tf.random_uniform([500], -10, 10, tf.float64))
sik3 = tf.add(tf.matmul(sik2, a3), b3)
sik3 = tf.nn.relu(sik3)

# [0, 0, 100, 30, 1] -> [1, 0]
# 다음층이 없으니 어차피 더 이상 계산 없음
# 최종 결과낼때 최대값이 있는 인덱스를 찾고
# => 활성화 함수 필요없을 것
a4 = tf.Variable(tf.random_uniform([500, len(yData[0])], -10, 10, tf.float64))
b4 = tf.Variable(tf.random_uniform([len(yData[0])], -10, 10, tf.float64))
sik4 = tf.add(tf.matmul(sik3, a4), b4)

# 실제 y, sik을 통해서 구해진거 거리
d = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=sik4))

ao = tf.train.AdamOptimizer(learning_rate=0.000001)
goal = ao.minimize(d)
################################################################
s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    dd = s.run(d, {x:xData, y:yData})
    print(dd)
    print("-----")
    
    if dd < 0.01:
        break
################################################################ 입력층 1, 은닉층 3, 출력층 1
a = float(input("싸움 : "))
b = float(input("욕 : "))
predictData = [[a, b]]

result = s.run(tf.argmax(sik4, 1), {x:predictData}) # list형태
print(label[result[0]])

resulttt = s.run(sik4, {x:predictData})
print(resulttt)