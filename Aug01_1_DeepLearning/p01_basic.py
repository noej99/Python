# -*- coding:utf-8 -*-

# 머신러닝 : 알고리즘을 사람이 골라주는
# 딥러닝 :
#        인공신경망을 구성해서
#        알고리즘도 AI가 찾아내서

# tensorflow 2.x
#    안되는 컴이 많은(CPU/GPU)
#    신버전 나온다고 필드에서 갈아타나

# pip 업그레이드
#    python -m pip install --upgrade pip

# tensorflow 1.9
#    pip install tensorflow==1.9
######################################
import tensorflow as tf
# 1) 인공신경망 구성
a = tf.constant(12) # a라는 상수 만들어서 12(값이 안들어감)
b = tf.constant(23)
c = tf.add(a, b) # a + b 계산(실제 계산 안함)
d = tf.constant("ㅋ")
print(c)
######################################
# 2) 구성된 인공신경망에 학습데이터를 넣어서
#    최적의 알고리즘 찾아서
#    인공신경망을 완성
s = tf.Session() # 실행 세션
# aResult = s.run(a) # 실행세션을 통해 실행을 해야 실제 값 들어감
# print(aResult)
cResult = s.run(c) # 연관된거 다 실행됨
print(cResult)
dResult = s.run(d)
print(dResult.decode())
######################################
# 3) 예측


