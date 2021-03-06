from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
	url(r'^$', views.list_project, name='list'),
	url(r'^new/$', views.create, name='create'),
	url(r'^(?P<project_id>[0-9A-Z]+)/cancel/$', views.cancel, name='cancel')
)