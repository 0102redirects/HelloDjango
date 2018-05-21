from django.contrib import admin

# Register your models here.
from MyApp.models import Grade, Students



class StudentAdmin(admin.ModelAdmin):

    def gendershow(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    gendershow.short_description = '性别'

    # 显示哪些字段
    list_display = ['sname','sage','sinfo',gendershow]

    # 分页，每一页最多多少数据
    list_per_page = 3

    # 过滤器，过滤条件字段
    list_filter = ['sname','sage']

    # 搜索
    search_fields = ['sname',]

    # 排序
    ordering = ['sage',]
    pass

# 定制插入班级的时候的学生信息
class StudentInfo(admin.TabularInline):
    model = Students
    extra = 3

# 定制的是插入班级时，需同步插入的模型信息
class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentInfo]

    list_display = ['gname', 'gboynum', 'ggirlnum']
    search_fields = ['gname', ]

# admin.site.register(Students,StudentAdmin)
# admin.site.register(Grade,GradeAdmin)



class MyAdminSite(admin.AdminSite):
    site_header = '学生站点管理'
    site_url = '/welcome'
    site_title = '我爱派森'

# 实例化一个自定义的AdminSite
site = MyAdminSite()

# 使用自定义的AdminSite进行模型注册
site.register(Students,StudentAdmin)
site.register(Grade,GradeAdmin)