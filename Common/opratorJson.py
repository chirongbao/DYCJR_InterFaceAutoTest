import json
class opratorJson(object):
    def __init__(self):
        self.Jsondata = self.getJsonData()

    def getJsonData(self):
        with open('../file/data.json','r') as file:
            jsonData=json.load(file)
            return jsonData

    def getValue(self,key):
        return self.Jsondata[key]

if __name__ == '__main__':
    aa=opratorJson()
    print(aa.getValue('appcode'))

    print('测试update')