# -*- coding:utf-8
'''解析一个请求，包含
    url,method,headers.cookies.postData,queryString
'''
import requests
import json
import chardet
import os
from RequestEntity import requestEntity

path = os.path.dirname(os.path.abspath(__file__))
filename = 'gongyilink.lianjia.com.har'
filepath = os.path.join(path,filename)
#domain = 'gongyilink.lianjia.com'

def analy(content,domain):
    requestEntityList = []
    # with open(filepath,'r') as file:
    #     content = file.read()

    requestList = filter(content,domain)  #对请求内容进行过滤

    for request in requestList:
        request_type = getRequest_type(request)
        url = getUrl(request)
        params = getParams(request);
        cookies = getCookies(request)
        headers = getHeaders(request)
        data,jsontext,file = getPostData(request)

        requestEntityList.append(requestEntity(url=url,request_type=request_type,cookies=cookies,
                                               headers=headers,params=params,data=data,json=jsontext,file=file))   #将请求对象放入列表中

    # for entiry in requestEntityList:
    #     entiry.toString()

    return requestEntityList

'''过滤掉不符合条件的请求'''
def filter(content,domain):
    bianma = chardet.detect(content)['encoding']  # 获取文件编码
    content = content.decode(bianma)  # 对内容进行解码
    content = json.loads(content)
    requestList = content['log']['entries']

    for request in requestList[:]:     #遍历拷贝的list，操作原始的list
        url = getUrl(request)
        if domain not in url:
            requestList.remove(request)
        else:
            for item in ['.gif','.png','.jpg','.JPEG','.js','.css','.html','.php','.svg','.ico']:
                if item in url:
                    requestList.remove(request)

    return requestList


'''获取请求方式'''
def getRequest_type(request):
    method = request['request']['method']
    return method

'''获取请求url，将?后的参数部分去除'''
def getUrl(request):
    url = request['request']['url']
    if '?' in url:
        url = url.split('?')[0]
    return url

'''获取get请求的参数'''
def getParams(request):
    queryString = request['request']['queryString']
    params = {}
    if len(queryString):
        for item in queryString:
            params[item['name']] = item['value']

    return params


'''获取post请求参数'''
def getPostData(request):
    jsontext = {}
    data = {}
    file = {}
    if request['request'].has_key('postData'):
        postData = request['request']['postData']
        mimeType = postData.get('mimeType','application/x-www-form-urlencoded')  #没有mimeType默认为
        if mimeType == 'application/json':
            jsontext =  json.loads(postData['text'])
        elif mimeType == 'application/x-www-form-urlencoded':
            for param in postData['params']:
                data[param['name']] = param['value']
        else:
            pass

    return data,jsontext,file


'''获取cookies'''
def getCookies(request):
    cookiesList = request['request']['cookies']
    cookiesdict = {}
    if len(cookiesList):  #判断list是否为空，长度不为0则为true
        for cookie  in cookiesList:
            cookiesdict[cookie['name']] = cookie['value']   #逐个取出每一个cookie

    return cookiesdict

'''获取header，将cookie从里面剔除'''
def getHeaders(request):
    headersList = request['request']['headers']
    headersdict = {}
    if len(headersList):
        for header  in headersList:
            if header['name'] == 'Cookie':       #将cookie过滤掉
                continue
            else:
                headersdict[header['name']] = header['value']

    return headersdict


if __name__ == '__main__':
    analy()