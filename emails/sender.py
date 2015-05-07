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

def new_proposal(email, content):
	subject = 'New proposal from ' + content['company_contact'] + ' at ' + content['company_name']
	send(email, content, subject, 'new_proposal')

def project_pitched(email, content):
	subject = 'Thanks for submitting your proposal'
	send(email, content, subject, 'project_pitched')

def project_cancel(email, content):
	subject = content['customer_name'] +  ' has cancelled their project'
	send(email, content, subject, 'project_cancel')

def hired(email, content):
	subject = 'Congrats, you have been hired by ' + content['customer_name']
	send(email, content, subject, 'hired')

def rejected(email, content):
	subject = content['customer_name'] + ' decided to hire someone else'
	send(email, content, subject, 'rejected')

def message_for_customer(email, content):
	subject = 'You have a new message from ' + content['company_contact']
	send(email, content, subject, 'message_for_customer')

def message_for_company(email, content):
	subject = 'You have a new message from ' + content['customer_name']
	send(email, content, subject, 'message_for_company')

def request_for_service(email, content):
	subject = 'Job request from ' + content['customer_name']
	send(email, content, subject, 'request_for_service')
