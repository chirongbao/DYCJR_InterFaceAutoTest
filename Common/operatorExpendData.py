from Common.operateExcel import comRongBaoOpretorExcel
from Common.getExcelData import getExcelCellData
from Common.getpostrun import run
from jsonpath_rw import jsonpath,parse
class opreExpend(object):
    #根据case_id获取该行的数据
    def __init__(self,case_id):
        self.data_sheet = comRongBaoOpretorExcel()
        self.get_excelData = getExcelCellData()
        self.sendrun = run()
        self.case_id = case_id

    #通过case_id获取该行的数据
    def get_row_data_depend(self):
        return self.data_sheet.get_row_data(self.case_id)

    #执行依赖的数据，得到返回的结果
    def get_response_data(self):
        row_num = self.data_sheet.get_row_num(self.case_id)
        url = self.get_excelData.getinterfaceUrl(row_num)
        requestMethod = self.get_excelData.getismethod(row_num)
        header = self.get_excelData.getheader(row_num)
        request_data = self.get_excelData.getrequestData(row_num)
        return self.sendrun.getpost(url,requestMethod,header,data=request_data)['data']

    #拿到excel的依赖返回数据，与相应对比，拿到相应的值
    def get_response_data_value(self,row):
        expendData =  self.get_excelData.getResponseexpend(row)
        response_data = self.get_response_data()
        # print(response_data)
        json_exe = parse(expendData)
        modelData = json_exe.find(response_data)
        return [math.value for math in modelData][0]











if __name__ == '__main__':
    aa = opreExpend('dycjr-1')
    print(aa.get_response_data_value(2))