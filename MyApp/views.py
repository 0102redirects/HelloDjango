from django.http import HttpResponse
from django.shortcuts import render
from MyApp.models import Grade, Students


# Create your views here.


def welcome(request):
    # return HttpResponse('HelloDjango')

    # grade1 = Grade.objects.get(pk=1)
    # students = grade1.students_set.all()

    # 查询所有学生
    students = Students.objects.all()

    # 构造数据字典
    data={
        'students':students
    }

    # 将数据丢给templates/welcome.html进行渲染并呈现给用户
    return render(request,'welcome.html',context=data)