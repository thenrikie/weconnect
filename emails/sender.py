from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template import Context
from django.conf import settings

def _addContent(content):
	content['host_url'] = settings.EMAIL_CONTENT_URL
	return content

def send(email, content, subject, template):
	content = _addContent(content)

	html = render_to_string('emails/' + template + '.html', content)
	return send_mail(subject, html, settings.EMAIL_FROM, [email], html_message=html)

def signup_customer(email, content):
	send(email, content, 'Welcome to RatedFrog', 'signup_customer')


def signup_company(email, content):
	send(email, content, 'Welcome to RatedFrog', 'signup_company')



