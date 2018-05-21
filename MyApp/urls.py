from django.conf.urls import url
from MyApp import views

# 定义路由映射
urlpatterns = [

    # 请求http://127.0.0.1:8000/myapp/,交由MyApp下的views.py中的welcome函数处理
    url(r'^$', views.welcome)
]