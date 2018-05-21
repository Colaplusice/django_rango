#coding=UTF-8
from django.contrib import admin
from rango.models import Category,Page,UserProfile,article
# Register your models here.
class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug')

class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title','url')

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

    list_display = ('title','pub_date','slug')
admin.site.register(Category,CatAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
admin.site.register(article,ArticleAdmin)