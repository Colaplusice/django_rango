from django.conf.urls import patterns,include,url
from django.contrib import admin
import registration.backends.simple.urls
    # Examples:
    # url(r'^$', 'itcast_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
urlpatterns = patterns('',
                       # url(r'^$', include(admin.site.urls)),
                       url(r'^admin/',include(admin.site.urls)),
    url(r'^rango/',include('rango.urls')),
url(r'^accounts/', include('registration.backends.simple.urls')),
url(r'^ueditor/', include('DjangoUeditor.urls')),

)
