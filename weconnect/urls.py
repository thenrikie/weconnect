from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weconnect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^auth/', include('authentication.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
)
