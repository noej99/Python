# -*- coding:utf-8 -*-
from hanspell.spell_checker import check

# py-hanspell : 개인개발자가 만들어서 github에 올려놓은 거
#    github에 있는거 pip으로 설치하려면 컴에 git이 필요
#    pip install git+주소

t = "몽둥이 금지라구요??? 당연한 말씀 그럼 방망이? 몽둥이, 회초리, 공포의 쓴맛?!"
t += "집에 가고싶어요 저런... 쌤 저 롤스로이스 고스트 사주세요 네? 안된다구요... 네..."

a = check(t)
print(a) # 전체 결과
print("-----")
print(a.checked) # 교정된 결과
print("-----")
print(a.errors) # 몇 개 교정했나
print("-----")
# print(a.words) # (단어, 결과)의 tuple list
for w, r in a.words.items():
    print(w, r)