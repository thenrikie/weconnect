from django.shortcuts import render, redirect, get_object_or_404
from pitches import forms
from projects import forms as project_forms
from pitches.models import Pitch, Message, MessageAttachment
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from pitches.forms import Message as MessageForm
from emails import sender

# Create your views here.
def list_request(r):
	pitches = Pitch.objects.filter(company=r.user, state='waiting', archived=False)
	print(pitches)
	return render(r, 'pitches/list_request.html', { 'pitches': pitches})

def list_quote(r):
	pitches = Pitch.objects.filter(company=r.user, state='accepted', archived=False)
	return render(r, 'pitches/list_quote.html', { 'pitches': pitches})

def list_hired(r):
	pitches = Pitch.objects.filter(company=r.user, state='hired', archived=False)
	return render(r, 'pitches/list_hired.html', { 'pitches': pitches})

def list_archive(r):
	pitches = Pitch.objects.filter(company=r.user, archived=True)
	return render(r, 'pitches/list_archive.html', { 'pitches': pitches})

def accept(r, pitch_id):
	pitch = get_object_or_404(Pitch, pk=pitch_id)


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

			return HttpResponseRedirect(reverse('pitches:list_quote'))
			
	return render(r, 'pitches/accept.html', {'pitch': pitch, 'form' : form})

def reject(r, pitch_id):

	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, pk=pitch_id)

		if pitch.state != 'waiting':
			print('project not in waiting state!')
			return redirect('/')

		if  pitch.company != r.user:
			print('only company user can reject!')
			return redirect('/')

		pitch.change_state('company_rejected')
		pitch.archived = True
		
		pitch.save()
		return HttpResponseRedirect(reverse('pitches:list_request'))

	return redirect('/')

def archive(r, pitch_id):
	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, pk=pitch_id)

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

def show(r, pitch_id, messageForm=None):
	if not r.user.is_authenticated():
		return redirect('/')

	pitch = get_object_or_404(Pitch, pk=pitch_id)

	project = pitch.project
	messages = pitch.message_set.order_by('-created_at')
	if not messageForm:
		print('no message form')
		messageForm = MessageForm()

	#mark messages as read
	Message.objects.filter(read=False, pitch=pitch, recipient=r.user).update(read=True, updated_at=datetime.now())
	#print(pitch.message_set.first().attachment.first())

	if pitch.company == r.user:
		return render(r, 'pitches/show_company.html', {
			'project': project, 
			'pitch': pitch, 
			'form': messageForm, 
			'messages': messages
		})
		
	elif pitch.project.user == r.user:
		pitches = project.ready_pitch()
		cancel_form = project_forms.Cancel()
		return render(r, 'pitches/show_customer.html', {
			'project': project, 
			'pitch': pitch, 
			'pitches': pitches, 
			'form': messageForm, 
			'messages': messages, 
			'cancel_form' : cancel_form
		})
	else:
		print('No Access to this project')
		return redirect('/')


def hire(r, pitch_id):

	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, pk=pitch_id)
		project = pitch.project

		if  project.user != r.user:
			print('You have no permission to hire!')
			return redirect('/')

		pitches = project.ready_pitch()
		for this_pitch in pitches:
			if this_pitch != pitch:
				this_pitch.change_state('rejected');
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

		return HttpResponseRedirect(reverse('pitches:show', args=[pitch.id]))



def post_message(r, pitch_id):

	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, pk=pitch_id)

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

			return HttpResponseRedirect(reverse('pitches:show', args=[pitch.id]))
		else:
			print ('not valid message')
			return show(r, pitch.id, form)
	else:
		return redirect(reverse('pitches:show', args=[pitch_id]))

def download_attachment(r, pitch_id, message_id):
	from django.conf import settings
	message = get_object_or_404(Message, pk=message_id)

	#permission checking
	if str(message.pitch.id) != pitch_id or (message.pitch.company != r.user and message.pitch.project.user != r.user):
		return redirect("/")

	filename = message.attachment.first().file.name.split("/")
	filename = filename[-1]

	with open(settings.MEDIA_ROOT + message.attachment.first().file.name, 'rb') as fsock:
		response = HttpResponse(fsock)
		response['Content-Disposition'] = "attachment; filename=" + filename

	return response