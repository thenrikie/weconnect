from django.conf.urls import patterns, url

from authentication import views

urlpatterns = patterns('',
	url(r'^$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^register/business/$', views.register_business, name='register_business'),
	url(r'^register/business/details/$', views.register_business_details, name='register_business_details')
)