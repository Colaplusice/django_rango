#coding=utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itcast_project.settings")
import django
from django.utils import timezone
django.setup()
from rango.models import Category,Page,article


def populate():
    python_cat=add_cat('python')  #创建python 目录类
    add_page(cat=python_cat,title='official python tutorial',
             url='http://docs.python.org/2/tutorial/')

    add_page(cat=python_cat,title='how to think like a computer scientist'
             ,url='http://www.greenteapress.com/thinkpython/')

    add_page(cat=python_cat,title='Learn python in ten minutes',
             url='http://www.korokithakis.net/tutorials/python/')

    django_cat=add_cat('django')
    add_page(cat=django_cat,title='django Rocks',
             url='http://www.djangorocks.com/')
    add_page(cat=django_cat,title='How to Tango with Django',
             url='http://www.tangowithdjango.com/')

    frame_cat = add_cat("Other Frameworks")
    add_page(cat=frame_cat,title='Bottle',
             url='http://bottlepy.org/docs/dev/')
    add_page(cat=frame_cat,title='flask',
             url='http://flask.pocoo.org')
    test_cat=add_cat('test')

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.all():
            print "-{0}-{1}".format(str(c),str(p))

def add_page(cat,title,url,views=0):
    p=Page.objects.get_or_create(category=cat,title=title,url=url,views=views)
    return p
def add_cat(name):
    c=Category.objects.get_or_create(name=name)[0]
    if c.name=='python':
        c.views=128
        c.likes=64
        c.save()
    elif c.name=='django':
        c.views=64
        c.likes=32
        c.save()
    else:
        c.likes=16
        c.views=32
        c.save()
    return c

def newarticle():
    article_cat=add_cat('articles')
    print(timezone.now)
    add_article('by sd','樊佳亮大三的大叔大婶多2爱仕达大撒所多爱仕达奥所多',
                timezone.now(),views=int(2),cat=article_cat)
def add_article(title,content,pub_date,views,cat):
    c=article.objects.get_or_create(title=title,content=content,pub_date=pub_date,views=views,category=cat)[0]
    c.save()
    print('添加完成')
if __name__ == '__main__':
    #脚本文件 自动往数据库写东西? 也没有很自动啊，就是方法的调用
    print('starting rango script')
    # populate()
    newarticle()