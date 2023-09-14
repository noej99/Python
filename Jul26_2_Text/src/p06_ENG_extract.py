# -*- coding:utf-8 -*-
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

# 어간
# 다양하게 변화 -> 변화 일어나지 않는 앞부분
words = "play plays playing played"
ps = PorterStemmer()
for w in word_tokenize(words):
    print(w, ps.stem(w))
print("-------")

words = "variety variation variable"
for w in word_tokenize(words):
    print(w, ps.stem(w))
print("-------")

# 표제어 : 원형
# import nltk
# nltk.download("omw-1.4")
# nltk.download("wordnet")
words = "am are is"
wnl = WordNetLemmatizer()
for w in word_tokenize(words):
    print(w, wnl.lemmatize(w, wordnet.VERB))
print("-----")    
words = "say said saying says"
for w in word_tokenize(words):
    print(w, wnl.lemmatize(w, wordnet.VERB))


