from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.Schedule)
admin.site.register(models.Comment)
admin.site.register(models.Company_Comment)

# Category name field에 데이터가 입력되었을 때 자동으로 slug를 생성한다. 
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(models.Category, CategoryAdmin)
