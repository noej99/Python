# -*- coding:utf-8 -*-

# AI분야
#    Machine Learning
#        문제를 해결하는데 필요한 알고리즘을 사람이 지정해주는
#            비만도검사, 가위바위보, ...
#            좀 AI스러운 알고리즘 몇 개 소개
#    Deep Learning
#        문제를 해결하는데 필요한 알고리즘도 컴이 찾아내서
#           인공신경망 구성해서...

#    지도학습 : 인간들이 결과를 구해놓은거를 AI한테 학습시키고
#                그 AI한테 새로운 데이터를 넣어서 결과를 물어보는
#                기온30도 -> 더움
#                기온-5도 -> 추움
#                오늘 10도 -> ???
#    비지도학습 : AI한테 데이터 주고 알아서 결론 내보라고
#                우리반 프로젝트 조 짜달라
#############################################
# scikit-learn : 머신러닝 라이브러리
# pip install -U scikit-learn

# kNN(k-Nearest Neighbor)알고리즘
#    사람들은 분류할때 비슷한거 기준으로
#    학습데이터들을 그래프 상의 점으로 놓고
#    예측해봐야하는 데이터와 가장 가까운 k를 찾아서
#    다수결로 결론

import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier

trainData = np.array([[80, 20], [95,5], [10, 90], [90, 10], [5, 95]])
label = np.array(['액션','액션', '조폭', '액션', '조폭'])

knc = KNeighborsClassifier(3) # 가장 가까운 3개를 뽑아서
knc.fit(trainData, label) # 학습시키기

x = float(input("격투씬 비율 : "))
y = float(input("욕씬 비율 : "))
xy = np.array([[x,y]])
result = knc.predict(xy)[0] # 예측시키기

print(result)


