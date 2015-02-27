from django.conf.urls import patterns, include, url
from django.contrib import admin
from weconnect import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weconnect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='home:index'),
    url(r'^auth/', include('authentication.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('users.urls', namespace='users'))
)
