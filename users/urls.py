from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
	url(r'^$', views.profile, name='profile'),
	url(r'company/(?P<company_id>[0-9A-Z]+)/$', views.pub_profile, name='pub_profile'),
)