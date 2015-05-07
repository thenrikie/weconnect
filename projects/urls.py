from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
	url(r'^$', views.list_project, name='list'),
	url(r'^new/$', views.create, name='create'),
	url(r'^new/details/$', views.create_details, name='create_details'),
	url(r'^(?P<project_id>\d+)/cancel/$', views.cancel, name='cancel')
)