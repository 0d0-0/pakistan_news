from django.shortcuts import render,HttpResponse,redirect
from Pakistan.models   import  test   #导入数据库
import requests  
import time
from bs4 import BeautifulSoup
from . import to_get_content
# Create your views here.

def welcome(request):
    if request.method == "GET":
        return render(request,'welcome.html')

def catalogue(request):
    if request.method == "GET":
        return render(request,'catalogue.html')

#具体内容用一个模板即可
def history(request):
    if request.method == "GET":
        soup=to_get_content.to_get_content(request,'https://storyofpakistan.com/events/the-mughal-empire/')
        times=soup.find('h1')
        #times=soup.find_all(class_='.title-heading-left fusion-responsive-typography-calculated')        
        #for time in times:
            #test.objects.create(time)
        print(times)
        return render(request,'content.html',{"times":times})

