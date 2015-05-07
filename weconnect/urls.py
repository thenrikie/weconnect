from django.conf.urls import patterns, include, url
from django.contrib import admin
from weconnect import views

admin.site.site_header = 'RatedFrog Admin'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weconnect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='home_index'),
    url(r'^customer$', views.customer, name='home_customer'),
    url(r'^business/$', views.business, name='home_business'),

    url(r'^auth/', include('authentication.urls', namespace='auth')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('users.urls', namespace='users')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^pitches/', include('pitches.urls', namespace='pitches')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts'))

)
