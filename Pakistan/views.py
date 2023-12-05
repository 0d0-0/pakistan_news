from django.shortcuts import render,HttpResponse,redirect
#from Pakistan.models import test   #导入数据库
import re
import requests  
import time
from bs4 import BeautifulSoup
from . import to_get_content
# Create your views here.

def welcome(request):
    if request.method == "GET":
        return render(request,'welcome.html')

def catalogue(request):   #目录
    if request.method == "GET":
        return render(request,'index.html')

#具体内容用一个模板即可
def history(request):
    if request.method == "GET":
        soup=to_get_content.to_get_content(request,r'https://storyofpakistan.com/events/the-mughal-empire/')
        current=soup.find('body').text
        times=re.split('[^\w\s]',current)
        print(times)
        #times=soup.find_all(class_='.title-heading-left fusion-responsive-typography-calculated')        
        return render(request,'history.html')


def diplomacy(request):
    if request.method == "GET":
        soup=to_get_content.to_get_content(request,r'https://storyofpakistan.com/events/the-mughal-empire/')
        current=soup.find('body').text
        times=re.split('[^\w\s]',current)
        print(times)
        #times=soup.find_all(class_='.title-heading-left fusion-responsive-typography-calculated')        
        return render(request,'diplomacy.html')


def culture(request):
    if request.method == "GET":
        soup=to_get_content.to_get_content(request,r'https://storyofpakistan.com/events/the-mughal-empire/')
        current=soup.find('body').text
        times=re.split('[^\w\s]',current)
        print(times)
        #times=soup.find_all(class_='.title-heading-left fusion-responsive-typography-calculated')        
        return render(request,'culture.html')

