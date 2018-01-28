# -*- coding:utf-8 -*-

from analysis import analy
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fileDirectory=os.path.join(path, 'generate/static/file')
filename = 'hardatadict.py'
dictpath = os.path.join(fileDirectory,filename)

model = '{"url": "%(url)s",\n\t\t\t' \
            '"request_type":"%(request_type)s",\n\t\t\t' \
            '"params":%(params)s,\n\t\t\t' \
            '"data":%(data)s,\n\t\t\t' \
            '"headers":%(headers)s,\n\t\t\t' \
            '"json":%(json)s,\n\t\t\t' \
            '"file": %(file)s,\n\t\t\t' \
            '"timeout":3,\n\t\t\t' \
            '"cookies":%(cookies)s,\n\t\t\t' \
            '"status_code":200,\n\t\t\t' \
            '"json_response": %(json_response)s,\n\t\t\t' \
            '"content":%(content)s\n\t\t\t' \
            '}'

def generateDataDict(content,domain):
    requestEntityList = analy(content,domain)
    for entity in requestEntityList:
        namelist = entity.url.split('/')
        if namelist[-1] == '':
            dictname = namelist[-2]
        else:
            dictname = namelist[-2] + '_' + namelist[-1]    #取url后两个路径生成字典名字
        dict = (dictname + ' = ' +  model) % {'url':entity.url,'request_type':entity.request_type,'params':entity.params,
                                               'data':entity.data,'headers':entity.headers,'json':entity.json,'file':entity.file,
                                               'cookies':entity.cookies,'json_response':entity.json_response,'content':entity.content}
        with open(dictpath,'a') as file:    #将datadict写入
            file.write(dict)
            file.write('\n\n')

if __name__ == '__main__':
   pass

