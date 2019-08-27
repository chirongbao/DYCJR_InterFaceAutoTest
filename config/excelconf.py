class excelCol(object):
    caseid = 0
    modelname = 1
    urlname = 2
    isaction = 3
    requestMethod = 4
    isheader = 5
    dependid = 6
    dependdata = 7
    dependcloume = 8
    requestData = 9
    expectResult = 10
    actualResult = 11

def getCaseId():
    return excelCol.caseid

def getmodelname():
    return excelCol.modelname


def geturlname():
    return excelCol.urlname


def getisaction():
    return excelCol.isaction


def getmethod():
    return excelCol.requestMethod


def getisheader():
    return excelCol.isheader


def getdependid():
    return excelCol.dependid


def getdependdata():
    return excelCol.dependdata


def getdependcloume():
    return excelCol.dependcloume


def getrequestData():
    return excelCol.requestData


def getexpectResult():
    return excelCol.expectResult


def getactualResult():
    return excelCol.actualResult

def getheaderDataNo():
    header={
        'Content-Type':'application/json;charset=UTF-8'
    }
    return header
def getheaderDataYes():
    cookiesData={
        'Content-Type': 'application/json;charset=UTF-8',
        'X-di':'8b19164a4b32d41f',
        'vkey':'5awSYqp1rfCzjrzF8wH9PHK1R90xR4ITat0vDI4csfuMs0HCdcMPMBIr9Du+tObSlUXiMp6Z4yTauRiXyqV4cQ=='
    }
    return cookiesData