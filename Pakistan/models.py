from django.db import models
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
    text = models .TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
def __str__(self):
    """返回一个表示条目的简单字符串"""
class test(models.Model):
    times=models.TextField(verbose_name='历史时期' ,max_length=100)
# Create your models here.
'''class History(models.Model):
    """巴基斯坦的历史"""
    title=models.CharField(verbose_name='历史时期' ,max_length=20)
    text=models.TextField(verbose_name='历史',blank=True )
class Meta:
    verbose_name= 'history of Pakistan'
    verbose_name_plural=verbose_name'''
