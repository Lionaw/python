"""定义learning_logs的URL模式"""
from django.urls import path,include,re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    #主页
    re_path('^$',views.index,name='index'),
    #显示所有的主题
    re_path('topic/$',views.topics,name='topics'),
    #特定主题的详细页面
    re_path('^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #用于添加新主题的页面
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]

app_name = 'learning_logs'