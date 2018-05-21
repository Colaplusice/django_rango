from django.conf.urls import url,patterns
from rango import views
urlpatterns = patterns('',

    # rango/login
    url(r'^login/$', views.Login, name='login'),

    #/rango/2
    url(r'^(?P<pagenum>[\d\d-]+)/$', views.index, name='index'),

    # rango/logout/
    url(r'^logout/$', views.user_logout, name='logout'),

    # /rango/
    url(r'^$', views.index_1, name='index'),

    # /rango/about
    url(r'^about/$', views.about, name='abouts'),

    #/rango/category/2/
    url(r'^category/(?P<cat_name_slug>[\w\w-]+)/$',views.category,name='category'),

    # rango/add_cat
    url(r'^add_cat/$',views.add_cat,name='add_cat'),

    # rango/category
    url(r'^(?P<cat_name_slug>[\w\w-]+)/$',views.cat_article,name='cat_article'),

# rango/add_page
url(r'^add_page/$',views.add_page,name='add_page'),

    # rango/category/add_page/
    url(r'^category/(?P<cat_name_slug>[\w\w-]+)/add_page/$', views.add_page, name='add_page'),

    # rango/register
    url(r'^register/$',views.register,name='register'),


    # rango/restricted
    url(r'^restricted/', views.restricted, name='restricted'),



    #rango/search
    url(r'^search/$',views.search,name='search'),

    #rango/goto
    url(r'^goto/$',views.Track_url,name='goto'),

    #rango/likecategory
    url(r'^like_category/$',views.like_category,name='like_category'),

    #rango/suggest_category
    url(r'^suggest_category/$',views.suggest_category,name='suggest_category'),

    #rango/blog/blog_id
    url(r'^blog/(?P<blog_slug>[\w\w-]+)/$',views.blog,name='blog'),
                       )

