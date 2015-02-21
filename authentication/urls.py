from django.conf.urls import patterns, url

from authentication import views

urlpatterns = patterns('',
	url(r'^$', views.Login.as_view(), name='login'),
)