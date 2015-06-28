from django.conf.urls import patterns, url
from django.conf import settings
from authentication import views

urlpatterns = patterns('',
	url(r'^$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^register/customer$', views.register_customer, name='register_customer'),
	url(r'^register/business/$', views.register_business, name='register_business'),
    url(r'^reset-password/$', 
    	'django.contrib.auth.views.password_reset', 
		{
			'post_reset_redirect' : '/auth/reset-password/done',
			'template_name': 'auth/reset_password.html',
			'email_template_name': 'emails/reset_password.html',
			'html_email_template_name': 'emails/reset_password.html',
			'from_email': settings.EMAIL_FROM
		},
		name="password_reset"
	),
    url(r'^reset-password/done/$',
		'django.contrib.auth.views.password_reset_done',
		{
			'template_name': 'auth/reset_password_done.html',
		},
		name="password_reset_done"
	),
	url(r'^reset-password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
		'django.contrib.auth.views.password_reset_confirm', 
		{
			'template_name': 'auth/reset_password_confirm.html',
			'post_reset_redirect' : '/auth/reset-password/complete'
		},
		name="password_reset_confirm"
	),
	url(r'^reset-password/complete/$', 
		views.password_reset_complete,
		name='password_reset_complete'
	),
)