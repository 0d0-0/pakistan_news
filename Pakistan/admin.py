from django.contrib import admin
from .models import Logo
# Register your models here.
from .models import Topic,Entry
admin.site.register(Topic)   #后台引入Topic模块
admin.site.register(Entry)   #后台引入Entry模块

admin.site.site_header = '刘一凡凡管理后台'  # 设置header
admin.site.site_title = '刘一凡凡管理后台'   # 设置title
admin.site.index_title = '刘一凡凡管理后台'
 
admin.site.register(Logo)