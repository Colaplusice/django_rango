from django.conf.urls import url,patterns
from rango import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^s/$',views.index,name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='abouts'),
    url(r'^category/(?P<cat_name_slug>[\w\w-]+)/$',views.category,name='category'),
    url(r'^add_cat/$',views.add_cat,name='add_cat'),
url(r'^add_page/$',views.add_page,name='add_page'),
    url(r'^category/(?P<cat_name_slug>[\w\w-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^search/$',views.search,name='search'),
    url(r'^goto/$',views.Track_url,name='goto'),
    url(r'^like_category/$',views.like_category,name='like_category'),
    url(r'^suggest_category/$',views.suggest_category,name='suggest_category'),
                       )

