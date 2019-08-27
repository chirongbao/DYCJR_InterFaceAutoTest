import xlrd
from xlutils.copy import copy


class comRongBaoOpretorExcel(object):
    def __init__(self, sheetid=None):
        if sheetid == None:
            self.sheetid = 0
        else:
            self.sheetid = sheetid
        self.data = self.getSheetdata()

    # 获取sheet数据
    def getSheetdata(self):
        excelData = xlrd.open_workbook('../file/jiekouTest.xls')
        sheetData = excelData.sheet_by_index(self.sheetid)
        return sheetData

    # 获取cell数据
    def getSheetCellData(self, row, col):
        return self.data.cell_value(row, col)

    # 获取行号
    def getRowNum(self):
        return self.data.nrows

    # 将测试结果写入excel
    def writeExcel(self, row, col, value):
        readData = xlrd.open_workbook('../file/jiekouTest.xls')  # 获取excel的数据
        writeData = copy(readData)  # 将读取的数据复制一份，用于写入
        sheetData = writeData.get_sheet(0)  # 就是这样写的
        sheetData.write(row, col, value)
        writeData.save('../file/jiekouTest.xls')

    # 根据caseid获取对应的数据
    def get_row_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data

    # 根据行号获取对应的数据
    def get_row_value(self, row):
        return self.data.row_values(row)

    # 根据case_id获取行号
    def get_row_num(self, case_id):
        row_num = 0
        col_data = self.get_col_data()
        for i in col_data:
            if i == case_id:
                return row_num
            row_num+=1


    #获取某一列的值
    def get_col_data(self,col_id=None):
        if col_id == None:
            col_data = self.data.col_values(0)
        else:
            col_data = self.data.col_values(col_id)
        return col_data
    def get_coll_data(self):
        return self.data.col_values(0)


if __name__ == '__main__':
    aa = comRongBaoOpretorExcel()
    print(aa.get_row_data('dycjr-1'))
    # print(aa.get_col_data('dycjr-1'))
