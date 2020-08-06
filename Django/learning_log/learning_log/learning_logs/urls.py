"""定义learning_logs的URL模式"""
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    #主页
    re_path('^$',views.index,name='index'),
    #显示所有的主题
    re_path('topic/$',views.topics,name='topics'),
    #特定主题的详细页面
    re_path('^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #用于添加新主题的页面
    re_path('^new_topic/$',views.new_topic,name='new_topic'),
]

app_name = 'learning_logs'