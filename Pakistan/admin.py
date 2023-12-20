from django.contrib import admin

# Register your models here.
from .models import Topic,Entry
admin.site.register(Topic)   #后台引入Topic模块
admin.site.register(Entry)   #后台引入Entry模块