#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from rango.models import Page,Category,UserProfile
#传进一个参数
class CatForm(forms.ModelForm):
    name=forms.CharField(max_length=128,help_text='请输入类别名称')
    slug=forms.CharField(widget=forms.HiddenInput(),required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    def clean(self):
        cleaned_data=self.cleaned_data
        name=cleaned_data.get('name')
        print name
    class Meta:
        model=Category
        field=('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='请输入网页的标题')
    url = forms.URLField(max_length=200, help_text='请输入网页的地址')
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    class Meta:
     #model 建立 表单和模型的关联
         model=Page
         exclude=('category',)
    def clean(self):
        cleaned_data=self.cleaned_data
        url=cleaned_data.get('url')
        # if url and not url.startwith('http://'):
        #     url='http://'+url
        cleaned_data['url']= url
        return cleaned_data

#创建用户注册的表单
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        #关联Django的user类
        model=User
        fields=('username','email','password')
class UserProfileForm(forms.ModelForm):
    #关联rango 自己创建的UserProfile类
    class Meta:
        model=UserProfile
        fields=('website','picture')


