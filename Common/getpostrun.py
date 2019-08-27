import requests
import json

class run(object):
    def getrequest(self,url,header,data=None):
        if data == None:
            getrequestData = requests.get(url, headers=header).json()
        else:
            getrequestData = requests.get(url, params=data,headers=header).json()
        return getrequestData

    def postrequest(self,url,header,data):
            requestsData = json.dumps(data)
            postrequestData = requests.post(url, data=requestsData,headers=header).json()
            return postrequestData

    def getpost(self,url,method,header,data=None):
        if method == 'get':
            relresponse = self.getrequest(url,header,data)
        else:
            relresponse = self.postrequest(url,header,data)
        return relresponse

if __name__ == '__main__':
    # url='http://crmprovider.test.victorplus.cn/api/order/getPaperless'
    # data={"appCode":"SN190604155914000323"}
    # header = {'Content-Type': 'application/json;charset=UTF-8'}
    # responseData = requests.get(url,params=data,headers=header ).json()
    # print(responseData)
    url = 'http://crmapi-test.victorplus.cn/v3/order/personList'
    header = {'Content-Type': 'application/json;charset=UTF-8','X-di':'8b19164a4b32d41f',
              'vkey':'WrHcPODBilGJOqRr7GjIvZZZOg3VOP3dUjNxr6q9xBKCvUSioV1Gf4teGqTm0Bu43SfAl615EBF+g3TgZAV5CQ=='}
    data = {"type": "10001", "pageNo": 1, "pageSize": 10}
    # requestsData = json.dumps(data)
    # responseDta = requests.post(url,headers = header,data=requestsData).json()
    # print(responseDta)
    aa =  run()
    responseData = aa.getpost(url,'post',header,data)
    print(responseData)