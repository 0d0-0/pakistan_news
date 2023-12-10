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
class History(models.Model):
    """巴基斯坦的历史"""
    times=models.TextField(verbose_name='历史时期' ,max_length=100)
    text=models.TextField(verbose_name='历史内容',blank=True,null=True)
    #插入数据时间  精确点
    time_now=models.DateTimeField(verbose_name='更新时间',default=datetime.now())
    class Meta:
        verbose_name= 'history of Pakistan'
        verbose_name_plural=verbose_name

class Diplomacy(models.Model):
    '''巴基斯坦的外交'''
    country=models.TextField(verbose_name='国家',blank=True,null=True)
    title=models.TextField(verbose_name='标题',blank=True,null=True,unique=True)
    text=models.TextField(verbose_name='外交内容',blank=True,null=True)
    class Meta:
        verbose_name= 'diplomacy of Pakistan'
        verbose_name_plural=verbose_name

class Culture(models.Model):
    '''巴基斯坦的外交'''
    aspect=models.TextField(verbose_name='文化层面',blank=True,null=True,unique=True)
    text=models.TextField(verbose_name='文化内容',blank=True,null=True)
    class Meta:
        verbose_name= 'culture of Pakistan'
        verbose_name_plural=verbose_name

