"""
URL configuration for pakistan_news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pakistan import views

urlpatterns = [
    path('admin/', admin.site.urls),  #后台
    path('index/', views.index),  #https://pakistannews.cn/indx/也可进入主页面
    path('', views.index),  #https://pakistannews.cn/ 即可进入主页面
    path('history/', views.history),  #历史页面 链接
    path('culture/', views.culture),  #文化
    path('diplomacy/', views.diplomacy),  #外交
    path('login/', views.login_or_register, name='login_or_register'),
    #登录 或 注册 页面
]
                                                                                                                        