from Common.operateExcel import comRongBaoOpretorExcel
import config.excelconf
from Common.getpostrun import run
from Common.opratorJson import opratorJson
import json



class getExcelCellData(object):
    def __init__(self):
        self.opretorexcel = comRongBaoOpretorExcel()

    #获取行数
    def getExcelLines(self):
        return self.opretorexcel.getRowNum()

    #获取接口地址
    def getinterfaceUrl(self,row):
        col=config.excelconf.geturlname()
        interfaceurl = self.opretorexcel.getSheetCellData(row,col)
        return interfaceurl

    #获取是否需要执行
    def getisaction(self,row):
        col=config.excelconf.getisaction()
        interfaceisaction = self.opretorexcel.getSheetCellData(row,col)
        flag=None
        if interfaceisaction == 'yes':
            flag=True
        else:
            flag=False
        return flag

    #获取请求方式
    def getismethod(self,row):
        col = config.excelconf.getmethod()
        interfacemethod=self.opretorexcel.getSheetCellData(row,col)
        return interfacemethod

    #获取请求头
    def getheader(self,row):
        flag=None
        col = config.excelconf.getisheader()
        getisheader = self.opretorexcel.getSheetCellData(row,col)
        flag = None
        if getisheader == 'yes1':
            flag = config.excelconf.getheaderDataNo()
        else:
            flag = config.excelconf.getheaderDataYes()
        return flag

    #获取请求数据excel
    def getrequestData(self,row):
        col = config.excelconf.getrequestData()
        getreqData=self.opretorexcel.getSheetCellData(row,col)
        jsonObj = opratorJson()
        print(type(jsonObj.getValue(getreqData)))
        return jsonObj.getValue(getreqData)

    #获得预期结果
    def getExpectResult(self,row):
        col = config.excelconf.getexpectResult()
        expectData = self.opretorexcel.getSheetCellData(row,col)
        return expectData

    #测试结果写入excel
    def writeExcelData(self,row,value):
        col = config.excelconf.getactualResult()
        self.opretorexcel.writeExcel(row,col,value)

    #获取依赖的返回数据
    def getResponseexpend(self,row):
        col = config.excelconf.getdependdata()
        expendData = self.opretorexcel.getSheetCellData(row,col)
        if expendData == "":
            return None
        else:
            return expendData

    #获取依赖case_id
    def get_expend_caseid(self,row):
        col = config.excelconf.getdependid()
        expend_id = self.opretorexcel.getSheetCellData(row,col)
        if expend_id =='':
            return None
        else:
            return expend_id

    #获取依赖数据所属字段
    def get_expend_colum(self,row):
        col = config.excelconf.getdependcloume()
        return self.opretorexcel.getSheetCellData(row,col)






if __name__ == '__main__':
    aa=getExcelCellData()
    print(aa.getismethod(1))
    print(aa.getrequestData(1))

