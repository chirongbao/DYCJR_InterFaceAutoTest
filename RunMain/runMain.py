from Common.getExcelData import getExcelCellData
from Common.getpostrun import run
from Common.caseIsPass import Ispass
from Common.operatorExpendData import opreExpend
from Common.sendEmail import Send_Email
import json
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append("D:\githubCore\DYCJRInterfaceTest")




class runmain(object):
    def __init__(self):
        self.excelData=getExcelCellData()
        self.run = run()
        self.ispass = Ispass()
        self.sendemail = Send_Email()

    def runMainTest(self):
        caseNum = self.excelData.getExcelLines()
        pass_count = []
        fail_count = []

        for i in range(1,caseNum):
            url = self.excelData.getinterfaceUrl(i)
            isaction = self.excelData.getisaction(i)
            whetherMethod = self.excelData.getismethod(i)
            isheader = self.excelData.getheader(i)
            requestData = self.excelData.getrequestData(i)
            expectData = self.excelData.getExpectResult(i)
            expendCaseId = self.excelData.get_expend_caseid(i)

            if isaction:
                if expendCaseId != None:

                    self.opreteExpend = opreExpend(expendCaseId)
                    responseData = self.opreteExpend.get_response_data_value(i)
                    requestColum = self.excelData.get_expend_colum(i)
                    requestData[requestColum] = responseData
                requestContent = self.run.getpost(url,whetherMethod,header=isheader,data=requestData)
                print(requestContent)
                caseResult = self.ispass.inornotPass(expectData,requestContent['data'])
                # print(caseResult)

                if caseResult:
                    self.excelData.writeExcelData(i,'Success')
                    pass_count.append(i)
                else:
                    self.excelData.writeExcelData(i, json.dumps(requestContent))
                    fail_count.append(i)
        # print(str(pass_count)+'    '+'共'+str(len(pass_count))+''+'个success')
        # print(str(fail_count)+'    '+'共'+str(len(fail_count))+''+'个fail')
        self.sendemail.send_main(pass_count,fail_count)

if __name__ == '__main__':

    aa = runmain()
    rel = aa.runMainTest()
