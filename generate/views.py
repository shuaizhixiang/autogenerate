#-*-coding:utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import os
from har import generateDataDict

# Create your views here.

def har(request):
    return render(request,'base.html')

def json(request):
    return render(request,'json.html')

def script(request):
    return render(request,'script.html')

def demo(request):
    return render(request,'demo.html')

'''文件上传'''
def upload(request):
    if request.method == 'POST':
        domain = request.POST['domain']   #获取表单提交的数据
        db = request.POST['db']
        port = request.POST['port']
        file = request.FILES.get('file')  #获取表单提交的文件
        if not file:
            return HttpResponse('文件上传失败')
        else:
            fileContent = file.read()

        generateDataDict.generateDataDict(fileContent,domain)
        # apppath = os.path.dirname(os.path.abspath(__file__))
        # staticpath=os.path.join(apppath,'static')
        # filepath=os.path.join(staticpath,file.name)
        # with open(filepath,'wb') as f:
        #     for chunk in file.chunks(chunk_size=1024):   #将文件分块，然后写入保存
        #         f.write(chunk)

    return HttpResponseRedirect('/index')


if __name__ =='__main__':
    print os.path.abspath(__file__)
    path = os.path.dirname(os.path.abspath(__file__))
    staticpath = os.path.join(path, 'static')
    print staticpath