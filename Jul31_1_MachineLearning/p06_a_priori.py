# -*- coding:utf-8 -*-
from apyori import apriori

# a priori
#    비지도학습
#    연관관계(뭐랑 뭐랑 같이 잘 나오나)
#        마트 영수증 : 피자 -> 콜라
#    추천

# supportData(지지도)
#    30% 지정 -> 100명중 30명 이상은 산 물품만 대상으로
#    30명도 안 산 물품은 제외하고

# confidenceData(신뢰도)
#    50% 지정 -> 신뢰도가 50% 이상인것만 보자
#    피자를 산 사람이 콜라도 같이 살 확률 : 70%
#    치킨 산 사람이 피자도 같이 살 확률 : 10% - 빼고

# scikit-learn에 없어서
# pip inatall apyori

trainData = [["치킨", "맥주", "콜라"],
             ["치킨", "피자", "맥주", "콜라"],
             ["치킨", "콜라"],
             ["피자", "맥주"],
             ["맥주"],
             ["맥주", "소주"],
             ["막걸리", "맥주", "피자"],
             ["치킨", "피자"]]

# set : 중복x, 순서?
# frozenset : 수정못하는 set

result = apriori(trainData,
            min_support=0.4, # 5명중에 2명은 산 항목을 대상으로
            min_confidence=0.3 # 같이 살 확률이 30% 넘는것만 보자
        )
result = list(result)
for r in result:
    for r2 in r.ordered_statistics:
        print(list(r2.items_base), "산 사람이")
        print(list(r2.items_add), "도 같이 살 확률이")
        print(r2.confidence)
        print(r2.lift)
        print("-------")

# lift
#    같이 나올 확률/각각 따로 나올 확률
#    따로 나오는게 많냐 같이 나오는게 많냐


