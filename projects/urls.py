from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
	url(r'^new/$', views.create, name='create')
)