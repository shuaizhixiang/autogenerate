# -*- coding:utf-8

import os
import json
import chardet

def har():
    with open('C:\Users\Administrator\Desktop\gongyilink.lianjia.com.har','r') as file:
        content = file.read()

    print chardet.detect(content)
    #print type(content)
    #print content
    js = json.loads(content)
    requests = js['log']['entries']
    #print request
    #print type(requests)
    for request in requests :
        if 'lianjia.com' in request['request']['url']:
            for header in request['request']['headers']:
                #print header.values()
                #print type(header.values())
                if '*/*' in header.values() and 'Accept' in header.values():
                    print header.values()
                    print request['request']['url'],request['request']['method'],request['request']['queryString'],request['request']['headers']
                else:
                    continue


if __name__ == '__main__':
    har()