from django.db import models

# Create your models here.

# 班级类
class Grade(models.Model):

    # 班级名称
    gname = models.CharField(max_length=10)

    # 开班日期
    gdate = models.DateTimeField()

    # 女生数量
    ggirlnum = models.IntegerField()

    # 男生数量
    gboynum = models.IntegerField()

    # 是否已逻辑删除该班级
    isDelete = models.BooleanField(default=False)

    # 定义班级的打印输出信息
    def __str__(self):
        return self.gname

# 学生类
class Students(models.Model):
    # 学生姓名
    sname = models.CharField(max_length=20)

    # 学生性别
    sgender = models.BooleanField(default=True)

    # 学生年龄
    sage = models.IntegerField()

    # 备注信息
    sinfo = models.CharField(max_length=20)

    # 是否已逻辑删除该学生
    isDelete = models.BooleanField(default=False)

    # 学生所属的班级
    sgrade = models.ForeignKey(Grade)
