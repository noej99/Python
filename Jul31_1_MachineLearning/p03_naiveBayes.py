# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# naive bayes : 전문적이지 않은 베이지안 정리
#        지도학습
#        필터링용
#        결과가 A일 확률 vs B일 확률 vs C일 확률 따져서
#            확률 높은 쪽으로 결론

# 각 단어별로 그 단어때문에 욕일 확률 vs 정상일 확률 계산해서
trainData = ["you are a dog", "maybe not take him to dog park stupid", "my dalmation is so cute I love him", "I am a boy"]
label = ["욕", "욕", "정상", "정상"]

# 전처리
# BoW(Bag of Words) : 단어 수 세기
cv = CountVectorizer()
cvResult = cv.fit_transform(trainData)
cvResult = cvResult.toarray()
# print(cvResult)
print(cv.get_feature_names()) # 모든 단어들(중복빼고)
# print(cv.vocabulary_) # 단어:인덱스(횟수x)
# print(cv.vocabulary_["you"])
# print(cvResult)

predictData = [input("문장 : ")]
predictDataCvResult = cv.transform(predictData)
predictDataCvResult = predictDataCvResult.toarray()
# print(predictDataCvResult)

#################################
mnb = MultinomialNB()
mnb.fit(cvResult, label)
result = mnb.predict(predictDataCvResult)[0]
print(result)