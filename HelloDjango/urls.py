"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from HelloDjango import views
from MyApp.admin import site

# 分发路由请求
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', site.urls),

    # http://127.0.0.1:8000/请求交由HelloDjango下的views中的index函数处理
    url(r'^$',views.index),

    # http://127.0.0.1:8000/dameinv/请求交由HelloDjango下的views中的dameinv函数处理
    url(r'^dameinv/',views.dameinv),

    # http://127.0.0.1:8000/myapp/xxx统统交由MyApp下的urls重新分发
    url(r'^myapp/',include('MyApp.urls'))
]
