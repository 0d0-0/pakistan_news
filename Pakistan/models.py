from django.db import models
from datetime import datetime
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        """返回模型的字符串表示"""
        return self.text
    
class Entry(models.Model):
    """用户学习的主题具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
def __str__(self):
    """返回一个表示条目的简单字符串"""
class Test(models.Model):
    times=models.TextField(verbose_name='历史时期' ,max_length=100,unique=True)
    text=models.TextField(verbose_name='历史内容',blank=True,null=True)
    #插入数据时间  精确到秒
    time_now=models.DateTimeField(verbose_name='更新时间',default=datetime.now())
#Create your models here.
class History(models.Model):
    """巴基斯坦的历史"""
    times=models.TextField(verbose_name='历史时期' ,max_length=100,unique=True)
    text=models.TextField(verbose_name='历史内容',blank=True,null=True)
    #插入数据时间  精确到秒
    time_now=models.DateTimeField(verbose_name='更新时间',default=datetime.now())
    class Meta:
        verbose_name= 'history of Pakistan'
        verbose_name_plural=verbose_name
