# -*- coding:utf-8 -*-

# import
#    Java타입 : 옵션사항
#    Python타입 : 필수사항


class bear:
    def __init__(self, name):
        self.name = name

    def printInfo(self):
        print(self.name)

############################
if __name__ == "__main__":
    from animal.pet import cat
    c = cat("나비", 3)
    c.printInfo()
    
