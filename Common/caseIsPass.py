class Ispass(object):
    def inornotPass(self,expectResult,actualResult):
        flag = None
        if expectResult in actualResult:  #用in判断，列表可以，字典匹配的是key，而不是value
            flag = True
        else:
            flag = False
        return flag