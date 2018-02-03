#coding=UTF-8
from django.contrib import admin
from rango.models import Category,Page,UserProfile
# Register your models here.
class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug')

class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title','url')


admin.site.register(Category,CatAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)