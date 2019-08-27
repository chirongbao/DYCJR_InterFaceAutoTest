import requests
import json
class testDemo(object):
    def test(self):
        url = 'http://crmapi-test.victorplus.cn/v3/order/personList'
        headerData ={
                    'Content-Type':'application/json;charset=UTF-8',
                     'X-di':'8b19164a4b32d41f',
                     'vkey':'5awSYqp1rfCzjrzF8wH9PHK1R90xR4ITat0vDI4csfuMs0HCdcMPMBIr9Du+tObSlUXiMp6Z4yTauRiXyqV4cQ=='
                     }
        data = {'type': '10001','pageNo': 1,'pageSize': 10}
        requestData = json.dumps(data)

        responseData = requests.post(url,headers = headerData,data =requestData )
        print(responseData.text)

aa = testDemo()
aa.test()