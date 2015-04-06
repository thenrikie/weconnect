from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
	url(r'^$', views.profile, name='profile'),
	url(r'company/(?P<company_id>\d+)/$', views.pub_profile, name='pub_profile'),
)