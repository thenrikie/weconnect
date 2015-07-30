from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template import Context
from django.conf import settings
from authentication.models import User

def _addContent(content):
	content['host_url'] = settings.EMAIL_CONTENT_URL
	return content

def send(email, content, subject, template):
	content = _addContent(content)

	html = render_to_string('emails/' + template + '.html', content)
	return send_mail(subject, html, settings.EMAIL_FROM, [email], html_message=html)

def send_admin(content, subject, template):
	content = _addContent(content)

	emails = [user.email for user in User.objects.filter(groups__name='operator')]
	#print(emails)
	if len(emails) > 0:
		html = render_to_string('emails/' + template + '.html', content)
		return send_mail(subject, html, settings.EMAIL_FROM, emails, html_message=html)

	return True

def signup_customer(email, content):
	send(email, content, 'Welcome to RatedFrog', 'signup_customer')

def signup_customer_with_project(email, content):
	#print ('sending signup email')
	subject = 'Welcome to RatedFrog, we are already connecting you with ' + content['role'] + '\'s'
	send(email, content, subject, 'signup_customer_with_project')

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

def project_created_admin(content):
	subject = content['customer_name'] + ' <' +  content['customer_email'] + '> has submitted a project';
	send_admin(content, subject, 'project_created_admin')

def pitch_accepted_admin(content):
	#print('pitch_accepted_admin')
	subject = content['company_name'] + ' <' +  content['company_email'] + '> has submitted a proposal';
	send_admin(content, subject, 'pitch_accepted_admin')

def project_pitch_company_declined(content):
	subject = content['company_name'] + ' <' +  content['company_email'] + '> has chosen to pass on this project.';
	send_admin(content, subject, 'project_pitch_company_declined')

def project_pitch_customer_declined(content):
	subject = content['customer_name'] + ' <' +  content['customer_email'] + '> has declined proposal from ' + content['company_name'] + ' <' +  content['company_email'] + '>'
	send_admin(content, subject, 'project_pitch_customer_declined')

def hired_admin(content):
	subject = content['customer_name'] + ' <' +  content['customer_email'] + '> has hired ' + content['company_name'] + ' <' +  content['company_email'] + '>'
	send_admin(content, subject, 'hired_admin')

def project_cancel_admin(content):
	subject = content['customer_name'] + ' <' +  content['customer_email'] + '> has cancelled their project'
	send_admin(content, subject, 'project_cancel_admin')	

def contact_us_message(content):
	send_admin(content, "Someone just leave us a message", 'contact_us_message')	

def three_proposals_ready(content):
	#send 24 hours after 3 pitch ok
	#48, 48, 48
	subject = "You have 3 pending proposals for your " + content['project_type'] + " project"
	send(email, content, subject, 'three_proposals_ready')

def final_reminder_project(content):
	#14 after 3 ready
	subject = "Final Reminder: 3 " + content['role'] + " are still waiting to hear from you."
	send(email, content, subject, 'final_reminder_project')

def cancel_warning_project(content):
	#21 after 3 ready and auto cancel after 48hrs
	subject = "We will cancel your project in the next 48 hours"
	send(email, content, subject, 'cancel_warning_project')

def request_for_service_12hrs(content):
	subject = 'Job request from ' + content['customer_name']
	send(email, content, subject, 'request_for_service_12hrs')

def send_a_message_to_project(content):
	subject = 'We suggest sending a message to ' + content['customer_name']
	send(email, content, subject, 'send_a_message_to_project')
