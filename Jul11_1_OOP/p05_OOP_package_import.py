# -*- coding:utf-8 -*-

# J : 전세계적으로 많이 쓰이는
#     작업한거 공유하는 문화 -> maven
#     클래스명이 중복 될거고
#    package : 클래스명 중복될 때 구분
#            패키지명이 중복되면 방법이 없으니
#            필수로 com.회사명.프로그램명.주제
#    import : 패키지명 생략하고 싶을떄 쓰는 옵션사항


#############################################

# P : 전세계적으로 많이 쓰이는
#     작업한거 공유하는 문화(심지어 소스공개)
#     클래스명이 중복 될거고
#    package : 클래스명 중복될 때 구분
#            패키지명이 중복되면 방법이 없지만
#            그래도 상관x

#    import : 다른 모듈에 있는거 쓰려면 해야하는 필수사항
# import animal.pet             # import 패키지명.모듈명
# c = animal.pet.cat("나비", 3) # 패키지명.모듈명.클래스명
# c.printInfo()


# import animal.pet as ap # import 패키지명.모듈명 as 별칭
# c = ap.cat("나비", 3)   # 별칭.클래스명...
# c.printInfo()

from animal.pet import cat # from 패키지명.모듈명 import 가져올거
from animal.pet import dog
c = cat("나비", 3)         # 클래스명...
c.printInfo()
 
# class dog():
#     pass
 
d = dog() # 클래스명/함수명 중복되면 가까이 있는거
d.printInfo()

# from animal.pet import cat as apc
# c = apc("나비", 3)
# c.printInfo()