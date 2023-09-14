# -*- coding:utf-8 -*-
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

s = "This eBook is for the use of anyone anywhere in the United States and "
s += "most other parts of the world at no cost and with almost no restrictions "
s += "whatsoever. You may copy it, give it away or re-use it under the terms "
s += "of the Project Gutenberg License included with this eBook or online at "
s += "www.gutenberg.org. If you are not located in the United States, you "
s += "will have to check the laws of the country where you are located before "
s += "using this eBook."

# 품사 태깅 해줄거 다운(처음 한번만)
# import nltk
# nltk.download("averaged_perceptron_tagger")

wt = word_tokenize(s)
wt2 = pos_tag(wt)
for w, p in wt2:
    print(w, p)

