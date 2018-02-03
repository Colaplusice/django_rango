#coding=UTF-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from rango.models import Category
# Create your tests here.
from rango.views import add_cat
from rango.models import Category
class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        #保证了观测量不能为0
        cat=Category(name='test',views=-1,likes=0)
        cat.save()
        self.assertEqual((cat.views>=0),True)

    def test_slug_line_creation(self):
        cat=Category('Random Category String')
        cat.save()
        self.assertEqual(cat.slug,'Random-Category-String')
    # 测试Index页面有没有 返回参数为 not categories的时候
    def test_index_view_with_no_categories(self):
        # reverse 找到对应的url
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'],[])
    def add_cat(name,views,likes):
        c=Category.objects.get_or_create(name=name)
        c.views=views
        c.likes=likes
        c.save()
        return c
    def test_index_view_with_categories(self):
        add_cat('test',1,1)
        add_cat('temp',1,1)
        add_cat('tmp',1,1)
        add_cat('tmp test tmp',1,1)
        # self.client 模拟客户端
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'tmp test tmp')
        num_cats=len(response.context['categories'])
        self.assertEqual(num_cats,4)

