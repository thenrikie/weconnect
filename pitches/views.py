from django.shortcuts import render, redirect, get_object_or_404
from pitches import forms
from projects import forms as project_forms
from pitches.models import Pitch, Message, MessageAttachment
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from pitches.forms import Message as MessageForm
from emails import sender
from emails.models import Queue
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_request(r):
	if not r.user.is_company:
		return redirect("/")

	pitches = Pitch.objects.filter(company=r.user, state='waiting', archived=False).order_by('-created_at')
	return render(r, 'pitches/list_request.html', { 'pitches': pitches})

@login_required
def list_quote(r):
	if not r.user.is_company:
		return redirect("/")

	pitches = Pitch.objects.filter(company=r.user, state='accepted', archived=False).order_by('-created_at')
	return render(r, 'pitches/list_quote.html', { 'pitches': pitches})

@login_required
def list_hired(r):
	if not r.user.is_company:
		return redirect("/")

	pitches = Pitch.objects.filter(company=r.user, state='hired', archived=False).order_by('-created_at')
	return render(r, 'pitches/list_hired.html', { 'pitches': pitches})

@login_required
def list_archive(r):
	if not r.user.is_company:
		return redirect("/")

	pitches = Pitch.objects.filter(company=r.user, archived=True).order_by('-created_at')
	return render(r, 'pitches/list_archive.html', { 'pitches': pitches})

@login_required
def accept(r, pitch_id):
	pitch = get_object_or_404(Pitch, uniqid=pitch_id)


	if pitch.state != 'waiting':
		print('project not in waiting state!')
		return redirect('/')

	if  pitch.company != r.user:
		print('only company user can accept!')
		return redirect('/')

	form = forms.Accept()
	print(form.fields['desc'])
	if r.method == 'POST':
		form = forms.Accept(r.POST)
		if form.is_valid():
			print("Valid form")
			pitch.desc = form.cleaned_data['desc']
			pitch.rate = form.cleaned_data['rate']
			pitch.price = form.cleaned_data['price']
			pitch.change_state('accepted')

			pitch.save()
			#send emails to project creator
			sender.new_proposal(pitch.project.user.email, {
				'name' : pitch.project.user.first_name,
				'pitch': pitch,
				'company_contact': pitch.company.full_name(),
				'company_name' : pitch.company.userprofile.business_name,
				'project_type' : pitch.project.sub_business.first()
			})

			sender.project_pitched(r.user.email, {
				'name' : r.user.first_name,
				'customer_name': pitch.project.user.first_name
			})

			#send email to notify admin
			sender.pitch_accepted_admin({
				'company_email': pitch.company.email,
				'company_name' : pitch.company.userprofile.business_name,
				'pitch_id': pitch.id
			})

			#if this is the third pitch, add reminder to email queue
			print("pitch count:: " + str(pitch.project.pitch_count()))
			if pitch.project.pitch_count() >= 3:

				email_items = (
					{'day': 1, 'action': 'three_proposals_ready'},
					{'day': 3, 'action': 'three_proposals_ready'},
					{'day': 5, 'action': 'three_proposals_ready'},
					{'day': 7, 'action': 'three_proposals_ready'},
					{'day': 14, 'action': 'final_reminder_project'},
					{'day': 21, 'action': 'cancel_warning_project'},
				)

				for email_item in email_items:
					q = Queue(
						item_id=pitch.project.id,
						item_object='project',
						start_at = datetime.datetime.now() + datetime.timedelta(days=email_item['day']),
						before_at = datetime.datetime.now() + datetime.timedelta(days=email_item['day']+1),
						action = email_item['action']
					)
					
					q.save()


				for pitch in pitch.project.ready_pitch():
					q = Queue(
						item_id=pitch.id,
						item_object='pitch',
						start_at = datetime.datetime.now() + datetime.timedelta(days=3),
						before_at = datetime.datetime.now() + datetime.timedelta(days=4),
						action = 'send_a_message_to_project'
					)

					q.save()

			return HttpResponseRedirect(reverse('pitches:list_quote'))
			
	return render(r, 'pitches/accept.html', {'pitch': pitch, 'form' : form})

@login_required
def reject(r, pitch_id):

	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, uniqid=pitch_id)

		if pitch.state != 'waiting':
			print('project not in waiting state!')
			return redirect('/')

		if  pitch.company != r.user:
			print('only company user can reject!')
			return redirect('/')

		pitch.change_state('company_rejected')
		pitch.archived = True
		
		pitch.save()

		#notify admin
		sender.project_pitch_company_declined({
			'company_email': pitch.company.email,
			'company_name' : pitch.company.userprofile.business_name,
			'pitch_id': pitch.id,
			'project_type' : pitch.project.sub_business.first(),
			'project_id' : pitch.project.id
		})

		return HttpResponseRedirect(reverse('pitches:list_request'))

	return redirect('/')

@login_required
def archive(r, pitch_id):
	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, uniqid=pitch_id)

		if pitch.state == 'waiting':
			print('project in waiting state!')
			return redirect('/')

		if  pitch.company != r.user:
			print('only company user can archive!')
			return redirect('/')

		pitch.archived = True
		pitch.save()

		return  HttpResponseRedirect(reverse('pitches:list_archive'))

	return redirect('/')

@login_required
def show(r, pitch_id, messageForm=None):

	pitch = get_object_or_404(Pitch, uniqid=pitch_id)

	project = pitch.project
	messages = pitch.message_set.order_by('-created_at')
	if not messageForm:
		print('no message form')
		messageForm = MessageForm()

	#mark messages as read
	Message.objects.filter(read=False, pitch=pitch, recipient=r.user).update(read=True, updated_at=datetime.datetime.now())
	#print(pitch.message_set.first().attachment.first())

	if pitch.company == r.user:
		return render(r, 'pitches/show_company.html', {
			'project': project, 
			'pitch': pitch, 
			'form': messageForm, 
			'messages': messages
		})
		
	elif pitch.project.user == r.user and not pitch.waiting():
		pitches = project.ready_pitch()
		cancel_form = project_forms.Cancel()
		return render(r, 'pitches/show_customer.html', {
			'project': project, 
			'pitch': pitch, 
			'pitches': pitches, 
			'form': messageForm, 
			'messages': messages, 
			'cancel_form' : cancel_form,
			'popup_cancel': r.GET.get('cancel', None)
		})
	else:
		print('No Access to this project')
		return redirect('/')


@login_required
def hire(r, pitch_id):

	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, uniqid=pitch_id)
		project = pitch.project

		if  project.user != r.user:
			print('You have no permission to hire!')
			return redirect('/')

		pitches = project.ready_pitch()

		for this_pitch in pitches:
			if this_pitch != pitch and not this_pitch.rejected():
				this_pitch.change_state('rejected');
				this_pitch.archived = True
				this_pitch.save()

				sender.rejected(this_pitch.company.email, {
					'name' : this_pitch.company.first_name,
					'customer_name': this_pitch.project.user.first_name
				})


		pitches = project.waiting_pitch()
		
		for this_pitch in pitches:
			if this_pitch != pitch and not this_pitch.rejected():
				this_pitch.archived = True
				this_pitch.save()
				sender.rejected(this_pitch.company.email, {
					'name' : this_pitch.company.first_name,
					'customer_name': this_pitch.project.user.first_name
				})
		
		pitch.change_state('hired')
		pitch.save()

		sender.hired(pitch.company.email, {
			'name' : pitch.company.first_name,
			'customer_name': pitch.project.user.first_name
		})

		#notify admin
		sender.hired_admin({
			'company_email': pitch.company.email,
			'company_name' : pitch.company.userprofile.business_name,
			'pitch_id': pitch.id,
			'project_type' : pitch.project.sub_business.first(),
			'project_id' : pitch.project.id,
			'customer_name': pitch.project.user.full_name(),
			'customer_email': pitch.project.user.email
		})

		return HttpResponseRedirect(reverse('pitches:show', args=[pitch.uniqid]))

@login_required
def decline(r, pitch_id):
	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, uniqid=pitch_id)
		project = pitch.project

		if  project.user != r.user:
			print('You have no permission to decline!')
			return redirect('/')

		pitch.change_state('rejected');
		pitch.archived = True
		pitch.save()

		sender.rejected(pitch.company.email, {
			'name' : pitch.company.first_name,
			'customer_name': pitch.project.user.first_name
		})

		#notify admin
		sender.project_pitch_customer_declined({
			'company_email': pitch.company.email,
			'company_name' : pitch.company.userprofile.business_name,
			'pitch_id': pitch.id,
			'project_type' : pitch.project.sub_business.first(),
			'project_id' : pitch.project.id,
			'customer_name': pitch.project.user.full_name(),
			'customer_email': pitch.project.user.email
		})

	return HttpResponseRedirect(reverse('pitches:show', args=[pitch.uniqid]))

@login_required
def post_message(r, pitch_id):

	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, uniqid=pitch_id)

		if pitch.waiting():
			print('You cannot leave message while pitching is in waiting state')
			return redirect('/')

		if pitch.company != r.user and pitch.project.user != r.user:
			print('You have no permission to post message on this pitch')
			return redirect('/')

		form = MessageForm(r.POST, r.FILES)
		if form.is_valid():
			message = Message()
			message.content = form.cleaned_data['content']
			message.pitch = pitch
			message.sender = r.user
			message.recipient = pitch.company

			if message.sender == message.recipient:
				message.recipient = pitch.project.user
		
			message.save()

			print(message.id)
			if message.recipient == pitch.company:
				sender.message_for_company(pitch.company.email,{
					'name': pitch.company.first_name,
					'customer_name': r.user.first_name,
					'project_type': pitch.project.sub_business.first(),
					'message' : message.id,
					'pitch': pitch
				})

			elif message.recipient == pitch.project.user:
				sender.message_for_customer(pitch.project.user.email,{
					'name': pitch.project.user.first_name,
					'company_contact': pitch.company.first_name,
					'company_name': pitch.company.userprofile.business_name,
					'project_type': pitch.project.sub_business.first(),
					'message' : message.id,
					'pitch': pitch
				})

			if r.FILES.get('file'):
				message.attachment.add(MessageAttachment(file=r.FILES.get('file')))

			return HttpResponseRedirect(reverse('pitches:show', args=[pitch.uniqid]))
		else:
			print ('not valid message')
			return show(r, pitch.id, form)
	else:
		return redirect(reverse('pitches:show', args=[pitch_id]))

@login_required
def download_attachment(r, pitch_id, message_id):
	from django.conf import settings
	message = get_object_or_404(Message, id=message_id)

	#permission checking
	if str(message.pitch.uniqid) != pitch_id or (message.pitch.company != r.user and message.pitch.project.user != r.user):
		return redirect("/")

	filename = message.attachment.first().file.name.split("/")
	filename = filename[-1]

	with open(settings.MEDIA_ROOT + message.attachment.first().file.name, 'rb') as fsock:
		response = HttpResponse(fsock)
		response['Content-Disposition'] = "attachment; filename=" + filename

	return response