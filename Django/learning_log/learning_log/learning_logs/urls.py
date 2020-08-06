"""定义learning_logs的URL模式"""
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    #主页
    re_path('^$',views.index,name='index')
]

app_name = 'learning_logs'