from django.conf.urls import patterns, url
from pitches import views

urlpatterns = patterns('',
	url(r'^$', views.list_request, name='list_request'),
	url(r'^/request/$', views.list_request, name='list_request'),
	url(r'^/quote/$', views.list_request, name='list_quote'),
	url(r'^/hired/$', views.list_request, name='list_hired'),
	url(r'^/archive/$', views.list_request, name='list_archive'),
	
	url(r'^(?P<pitch_id>\d+)/accept/$', views.accept, name='accept'),
	url(r'^(?P<pitch_id>\d+)/reject/$', views.reject, name='reject')
)