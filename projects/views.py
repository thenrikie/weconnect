from django.shortcuts import render, redirect, get_object_or_404
from projects import forms
from pitches.forms import Message as MessageForm
from authentication.forms import Register
from authentication.views import create_customer
from projects.models import Project, Question, QuestionOption
from users.models import Business, SubBusiness
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from emails import sender
import json

# Create your views here.


def create(r):
	return create_project_select_business(r)

def create_details(r):
	return create_project_select_details(r);


def create_project_select_business(r):
	subBusinesses = SubBusiness.objects.all();
	sub_business_json = json.dumps([ob.as_json() for ob in subBusinesses])

	form = forms.Business()

	if r.method == 'POST':
		form = forms.Business(r.POST)
		if form.is_valid():
			r.session['create_project_business'] = { 'business' : form.cleaned_data['business'].id, 'sub_business': r.POST['sub_business']}
			return redirect('projects:create_details')

	return render(r, 'projects/create_project_select_business.html', {'form' : form, 'sub_business_json': sub_business_json})

def create_project_select_details(r):
	
	#get session from first create page
	session_business = r.session.get('create_project_business')

	if not session_business or not session_business.get('business') or not session_business.get('sub_business'):
		return redirect('projects:create')

	#get question set based on business selected
	questions = Question.objects.filter(sub_business=session_business['sub_business'])
	extra = []

	for q in questions:
		extra.append({'question': q.text, 'type': q.type, 'queryset': QuestionOption.objects.filter(question=q)})

	questionForm = forms.ProjectQuestion(r.POST or None, extra=extra);
	form = forms.Project(r.POST or None)
	registerForm = Register(r.POST or None)

	#check if logged in
	loggedIn = False
	if r.user.is_authenticated():
		loggedIn = True

	if r.method == 'POST':
		if form.is_valid() and questionForm.is_valid() and (loggedIn or registerForm.is_valid()):
			print('passed')

			if not loggedIn:
				print('Not logged in, create user first')
				user = create_customer(r.POST)
				if user is not None and user.is_active:
					auth.login(r, user)
					sender.signup_customer(user.email, {'name': user.full_name()})
				else:
					return redirect('/')

			whiteListProject = {k: r.POST.get(k, False) for k in (
				'urgency', 
				'can_travel', 
				'company_travel',
				'budget_lower',
				'budget_upper',
				'desc'
				)
			}

			project = Project(user=r.user, my_place=form.cleaned_data['my_place'], **whiteListProject)
			project.save()

			project.business.add(session_business['business'])

			##for var in form.cleaned_data['sub_business']:
			##	project.sub_business.add(var)
			project.sub_business.add(session_business['sub_business'])

			for var in form.cleaned_data['travel_distance']:
				project.travel_distance.add(var)

			#save question option
			for key, question_set in questionForm.cleaned_data.items():
				try: 
					for question in question_set:
						project.question_option.add(question)
				except TypeError:
					project.question_option.add(question_set)

			del r.session['create_project_business']
			
			return redirect('projects:list')

		#print("post not passed")

	return render(r, 'projects/create_project_select_details.html', {'form' : form, 'questionForm': questionForm, 'registerForm': registerForm})

def list_project(r):

	if not r.user.is_authenticated():
		return redirect('/')

	projects = Project.objects.all().filter(user=r.user)
	return render(r, 'projects/list.html', {'projects' : projects})

def cancel(r, project_id):

	if r.method != 'POST':
		return redirect('/')

	if not r.user.is_authenticated():
		return redirect('/')

	project = get_object_or_404(Project, pk=project_id)
	project.cancelled = True
	form = forms.Cancel(r.POST, instance=project)

	if form.is_valid():
		print('passed')
		form.save()
		#update all pitches status
		pitches = project.ready_pitch()

		for pitch in pitches:
			pitch.change_state('rejected')
			pitch.archived = True
			pitch.save()
			sender.project_cancel(pitch.company.email, {
				'name' : pitch.company.first_name,
				'customer_name': project.user.first_name,
				'project_type': project.sub_business.first()
			})
		
		return redirect('projects:list')
	else:
		return redirect('/')