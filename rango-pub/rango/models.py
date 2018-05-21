# coding=UTF-8
import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from DjangoUeditor.models import UEditorField
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=128,unique=True)
    views=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    slug=models.SlugField(unique=True)
    def save(self,*args,**kwargs):
        if  self.views<0:
            print('false')
            self.views=0
        #slugify 去除空格 让目录的名字作为他的slug属性
        self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)
    def __unicode__(self):
        return self.name
class Page(models.Model):
    category=models.ForeignKey(Category)
    title=models.CharField(max_length=128)
    url=models.URLField()
    views=models.IntegerField(default=12)
    def __unicode__(self):
        return self.title
    #用户信息类
class UserProfile(models.Model):
    user=models.OneToOneField(User)
    website=models.URLField(blank=True)
    picture=models.ImageField(upload_to='profile_images',blank=True)

    def __unicode__(self):
        return self.user.username

class article(models.Model):
    title=models.CharField(max_length=128,unique=True)
    pub_date=models.DateTimeField(default=timezone.now)
    content=models.TextField('内容')
    views=models.IntegerField(default=0)
    category=models.ForeignKey(Category)
    slug=models.SlugField(unique=True)
    class Meta:
       ordering = ('-pub_date',)
    def __unicode__(self):
        return self.title