# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.cluster._kmeans import KMeans
# kMeans : k개의 평균
#        비지도학습
#        주어진 데이터들을 비슷한것끼리(clustering)

#        데이터들을 그래프상에 점 찍고(빨강)
#        k개의 랜덤한 점 찍고(초록)
#        초록-빨강 거리 구해서 가까운것끼리 군집화
#        그 군집 내에서 평균 구해서 k개의 초록점 다시

#        초록-빨강 거리 구해서 가까운것끼리 군집화
#        그 군집 내에서 평균 구해서 k개의 초록점 다시

#        ...초록 점이 더이상 안움직일때까지 반복
#        반복이 끝났을 때 군집을 최종 군집으로

# seaborn으로
df = pd.DataFrame()
df["싸움"] = [80, 95, 10, 90, 5]
df["욕"] = [20, 5, 90, 10, 95]
print(df)

trainData = df[["싸움", "욕"]].to_numpy()
print(trainData)

# 머신러닝 알고리즘 직접 구현하자
# 머신러닝 라이브러리 쓰자
km = KMeans(3)
df["그룹"] = km.fit_predict(trainData)
print(df)

# sns.scatterplot(x="싸움", y="욕", hue="그룹", data=df, palette="pastel")
# plt.show()
print("---------")

# kMeans로 라벨링 + kNN으로 예측
label = df["그룹"].to_numpy()
knc = KNeighborsClassifier(3)
knc.fit(trainData, label)

a = float(input("싸움 : "))
b = float(input("욕 : "))
predictData = np.array([[a, b]])

result = knc.predict(predictData)[0]
print(result)




