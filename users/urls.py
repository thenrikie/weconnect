from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
	url(r'^$', views.profile, name='profile'),
	url(r'^company/(?P<company_id>[0-9A-Z]+)/$', views.pub_profile, name='pub_profile'),
	url(r'^showcases/(?P<showcase_id>\d+)/delete$', views.delete_showcase, name='delete_showcase'),
	url(r'^showcase-attachments/(?P<showcase_attachment_id>\d+)/delete$', views.delete_showcase_attachment, name='delete_showcase_attachment'),
)