# -*- coding:utf-8 -*-
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# 불용어(stopword) : 별 의미 없는것들
#    a, the, ...

s = "This eBook is for the use of anyone anywhere in the United States and "
s += "most other parts of the world at no cost and with almost no restrictions "
s += "whatsoever. You may copy it, give it away or re-use it under the terms "
s += "of the Project Gutenberg License included with this eBook or online at "
s += "www.gutenberg.org. If you are not located in the United States, you "
s += "will have to check the laws of the country where you are located before "
s += "using this eBook."

# 불용어들 다운받기(처음 한번만)
# import nltk
# nltk.download("stopwords")

# 불용어들 list로
sw = stopwords.words("english")
print(sw)

# 불용어들 제외하고 단어수 세기
wordCountDict = {}
for word in word_tokenize(s):
    word = word.lower()
    
    if word not in sw:
        if word in wordCountDict:
            wordCountDict[word] += 1
        else:
            wordCountDict[word] = 1

for k, v in wordCountDict.items():
    print(k,v)
















