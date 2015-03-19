from django.conf.urls import patterns, url
from pitches import views

urlpatterns = patterns('',
	url(r'^$', views.list_request, name='list'),
	url(r'^request/$', views.list_request, name='list_request'),
	url(r'^quote/$', views.list_quote, name='list_quote'),
	url(r'^hired/$', views.list_hired, name='list_hired'),
	url(r'^archive/$', views.list_archive, name='list_archive'),

	url(r'^(?P<pitch_id>\d+)/accept/$', views.accept, name='accept'),
	url(r'^(?P<pitch_id>\d+)/reject/$', views.reject, name='reject'),
	url(r'^(?P<pitch_id>\d+)/archive/$', views.archive, name='archive'),
	url(r'^(?P<pitch_id>\d+)/hire/$', views.hire, name='hire'),

	url(r'^(?P<pitch_id>\d+)/$', views.show, name='show'),
	url(r'^(?P<pitch_id>\d+)/messages/$', views.post_message, name='post_message')

)