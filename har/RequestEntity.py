# -*- coding:utf-8 -*-


class requestEntity:
    def __init__(self,url,request_type,headers,cookies,params={},json={},data={},file = {},timeout = 3,
                 status_code = 200,json_response = {},content = {}):
        self.url = url
        self.request_type = request_type
        self.params = params
        self.data = data
        self.headers = headers
        self.json = json
        self.file = file
        self.timeout = timeout
        self.cookies = cookies
        self.status_code = status_code
        self.json_response = json_response
        self.content = content


    def toString(self):
        print 'url:',self.url
        print 'request_type:',self.request_type
        print 'params:',self.params
        print 'data:',self.data
        print 'headers:',self.headers
        print 'json:', self.json
        print 'file:', self.file
        print 'timeout:', self.timeout
        print 'cookies:', self.cookies
        print 'status_code:', self.status_code
        print 'json_response:', self.json_response
        print 'content:', self.content
        print ''