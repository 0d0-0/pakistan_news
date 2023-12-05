from django.shortcuts import render,HttpResponse,redirect
from Pakistan.models   import  test   #导入数据库
import requests
import time
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
def to_get_content(request,url):    #  爬取内容
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    #header代理标头  有些网页没有会拒绝请求
    #有些网站会重定向请求
    response = requests.get(url,allow_redirects=True,headers=headers)  #向url发送请求
    
    
    if response.status_code == 200:  #请求成功
        soup = BeautifulSoup(response.content,'html.parser') 
           # 解析网页内容  并获得所有内容
        return soup
    else :
        print("失败")
        time.sleep(1)  # 在失败的情况下休眠一秒 避免过于频繁
        return HttpResponse("失败")
    
# def save_data(data):
#     # 在这里将爬取到的数据保存到数据库、文件或其他存储介质中

# def classify_data(data):
#     # 在这里使用文本分类算法对数据进行分类
#     # 可以使用 CountVectorizer 将文本转换为向量表示
#     # 然后使用分类器（如朴素贝叶斯分类器）进行训练和预测
#     # 返回分类结果


# def start_crawling(urls):
#     for url in urls:
#         to_get_content(request,url)
#         category = classify_data(data)  #算法数据分类
#         save_data(category)