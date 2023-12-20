from django.db import models
from django.contrib import admin

class Topic(models.Model):  #显示在admin模块里 主题
    """用户学习的主题"""
    text = models.CharField(max_length=200)  #主题名称
    date_added = models.DateTimeField(auto_now_add=True) #添加时间
    def __str__ (self):    
        """返回模型的字符串表示"""
        return self.text
    
class Entry(models.Model):
    """用户学习的主题具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)   #引入Topic中的外键  主题 
    text = models.TextField()                 #主题之下的正文内容
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
def __str__(self):
    """返回一个表示条目的简单字符串"""

class Logo(models.Model):  #显示在admin模块里 主题
    def __str__ (self):    
        """返回模型的字符串表示"""
        return self.text

#在终端管理员中  ssh root@159.138.136.13
#cd python/pakistan_news/
#sqlite3 db.sqlite3
#.tables 查看都有哪些表
#select * from auth_user;查看用户
#select * from Pakistan_culture;查看文化内容
#select * from Pakistan_history;查看历史内容
#select * from Pakistan_diplomacy;查看外交内容
class History(models.Model):   #历史  建表   将数据放入sqlite3数据库中  在服务器中运行时可在终端命令行用select语句查看
    """巴基斯坦的历史"""
    times=models.TextField(verbose_name='历史时期' ,max_length=100)  #历史时期
    text=models.TextField(verbose_name='历史内容',blank=True,null=True)  #历史时期发生的内容
    class Meta:
        verbose_name= 'history of Pakistan'
        verbose_name_plural=verbose_name

class Diplomacy(models.Model):  #外交建表 将数据放入sqlite3数据库中  在服务器中运行时可在终端命令行用select语句查看
    '''巴基斯坦的外交'''
    country=models.TextField(verbose_name='国家',blank=True,null=True)
    title=models.TextField(verbose_name='标题',blank=True,null=True,unique=True)
    text=models.TextField(verbose_name='外交内容',blank=True,null=True)
    class Meta:
        verbose_name= 'diplomacy of Pakistan'
        verbose_name_plural=verbose_name

class Culture(models.Model):  #文化建表   将数据放入sqlite3数据库中  在服务器中运行时可在终端命令行用select语句查看
    '''巴基斯坦的外交'''
    aspect=models.TextField(verbose_name='文化层面',blank=True,null=True,unique=True)
    text=models.TextField(verbose_name='文化内容',blank=True,null=True)
    class Meta:
        verbose_name= 'culture of Pakistan'
        verbose_name_plural=verbose_name


class User(models.Model):   #建表
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


@admin.register(User)#装饰器 
class UserAdmin(admin.ModelAdmin): #将用户放入数据放入后台
    list_display = ('username', 'password') 
    #放入后台  在 '认证和授权'中的 用户一栏 点击查看和管理
    #也可在命令行中  select * from auth_user 查看