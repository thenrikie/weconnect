from django.conf.urls import patterns, url
from pitches import views

urlpatterns = patterns('',
	url(r'^$', views.list_request, name='list'),
	url(r'^request/$', views.list_request, name='list_request'),
	url(r'^quote/$', views.list_quote, name='list_quote'),
	url(r'^hired/$', views.list_hired, name='list_hired'),
	url(r'^archive/$', views.list_archive, name='list_archive'),

	url(r'^(?P<pitch_id>[0-9A-Z]+)/accept/$', views.accept, name='accept'),
	url(r'^(?P<pitch_id>[0-9A-Z]+)/reject/$', views.reject, name='reject'),
	url(r'^(?P<pitch_id>[0-9A-Z]+)/archive/$', views.archive, name='archive'),
	url(r'^(?P<pitch_id>[0-9A-Z]+)/hire/$', views.hire, name='hire'),
	url(r'^(?P<pitch_id>[0-9A-Z]+)/decline/$', views.decline, name='decline'),

	url(r'^(?P<pitch_id>[0-9A-Z]+)/$', views.show, name='show'),
	url(r'^(?P<pitch_id>[0-9A-Z]+)/messages/$', views.post_message, name='post_message'),
	url(r'^(?P<pitch_id>[0-9A-Z]+)/messages/(?P<message_id>\d+)/attachment$', views.download_attachment, name='download_attachment')


)