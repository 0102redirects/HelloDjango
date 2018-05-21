from django.http import HttpResponse
from django.shortcuts import render

# 处理http://127.0.0.1:8000/
def index(request):

    # 直接在页面输出内容
    return HttpResponse('Django：江中自有黄金屋，屋里把那代码撸，江中自有颜如玉，硬盘堆满几百G')

# 处理http://127.0.0.1:8000/dameinv/
def dameinv(request):

    # 渲染页面并呈现给用户
    return render(request,'dameinv.html')