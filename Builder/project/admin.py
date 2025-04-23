from django.contrib import admin
from project.models import Page, Project
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_by', 'created_on')
    list_filter = ('created_on','created_by')

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    
    list_display = ('id','content','project')
    list_filter = ('created_by','created_on','project')
