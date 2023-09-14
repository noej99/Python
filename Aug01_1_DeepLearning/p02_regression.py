# -*- coding:utf-8 -*-

# (1, 10), (2, 20), (3, 30), (5, 50) : y = 10x
# (1, 11), (2, 21), (3, 31), (5, 51) : y = 10x + 1
# (1, 12), (2, 19), (3, 30), (5, ?)  : y = ax + b

# regression(회귀분석) -> [인공신경망 : 다차원/다단 회귀분석]
#    주어진 점들을 최대한 만족시킬 회귀방정식(y = ax + b)
#    을 찾아서 그걸로 예측

import tensorflow as tf

xData = [1, 2, 3]
yData = [12, 19, 30]
################################################################
# 1) 인공신경망 구성
#    상수 : tf.constant()
#    변수
#        tf.placeholder() : 값 들어갈 자리(x, y)
#        tf.Variable() : AI가 찾아내야 할 값(a, b)
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

# 첫 값 지정

# 1차원, 그냥 0 -> 쌩 랜덤
a = tf.Variable(tf.zeros([1], tf.float64))

# 1차원, -2 ~ 3 사이 랜덤 -> 정규분포
b = tf.Variable(tf.random_uniform([1], -2, 3, tf.float64))

sik = a * x + b
# sik = 0x + 1.5
# sik x자리에 1 넣으면 1.5 : (1, 1.5)
# 실제                     : (1, 10)
# sik을 통해서 구한 y값 vs 실제 y값 비교
# 그 두 값이 최대한 차이가 없게 a/b값을 찾아내는게 목표
# => sik값, y값 거리가 최대한 짧아지게

# 거리 계산 해서 -> 차원수 줄이고, 평균
d = tf.reduce_mean(tf.square(y - sik))

# 최적의 값을 찾아줄 객체
#    learning_rate
#        값 크게 : 0 -> 100 -> -30 -> 50 -> 60 -> 300
#            빠름
#            정답을 지나칠수도 -> 영원히 못찾을수도
#        값 작게 : 0 -> 0.1 -> 0.2 -> 0.15
#            느림
#            정답은 무조건 찾을것
ao = tf.train.AdamOptimizer(learning_rate=0.0001)

# 반복적으로 a/b값을 바꿔가면서 d를 줄이는게 목표
goal = ao.minimize(d)
################################################################
# 2) 학습데이터 넣어서 최적의 알고리즘 찾기
s = tf.Session()
s.run(tf.global_variables_initializer()) # tf.Variable들 초기화

while True:
    s.run(goal, {x:xData, y:yData})
    
    # 확인용(실제로 필요는 x)
    print("y = %fx + %f" % (s.run(a), s.run(b)))
    dd = s.run(d, {x:xData, y:yData})
    print(dd)
    print("-----")
    
    if dd < 1:
        break
################################################################
# 3) 예측
newX = float(input("x : "))
result = s.run(sik, {x:newX})[0]
print(result)


