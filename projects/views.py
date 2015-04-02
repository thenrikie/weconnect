from django.shortcuts import render, redirect, get_object_or_404
from projects import forms
from pitches.forms import Message as MessageForm
from projects.models import Project, Question, QuestionOption
from users.models import Business, SubBusiness
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import json

# Create your views here.


def create(r):
	if not r.user.is_authenticated():
		return redirect('/')

	return create_project_select_business(r)

def create_details(r):
	if not r.user.is_authenticated():
		return redirect('/')
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
	

	session_business = r.session.get('create_project_business')

	if not session_business or not session_business.get('business') or not session_business.get('sub_business'):
		return redirect('projects:create');

	form = forms.Project()
	questions = Question.objects.filter(sub_business=session_business['sub_business'])
	extra = []

	for q in questions:
		extra.append({'question': q.text, 'type': q.type, 'queryset': QuestionOption.objects.filter(question=q)})

	questionForm = forms.ProjectQuestion(extra=extra);

	if r.method == 'POST':

		form = forms.Project(r.POST)

		print(r.POST)
		if form.is_valid():
			print('passed')

			whiteListProject = {k: r.POST.get(k, False) for k in (
				'urgency', 
				'can_travel', 
				'company_travel', 
				)
			}

			print(form.cleaned_data['my_place'])
			project = Project(user=r.user, my_place=form.cleaned_data['my_place'], **whiteListProject)
			project.save()

			project.business.add(businessForm.cleaned_data['business'])

			##for var in form.cleaned_data['sub_business']:
			##	project.sub_business.add(var)
			project.sub_business.add(session_business['sub_business'])

			for var in form.cleaned_data['travel_distance']:
				project.travel_distance.add(var)

			
			return HttpResponseRedirect(reverse('projects:list'))

		#print("post not passed")




	return render(r, 'projects/create_project_select_details.html', {'form' : form, 'questionForm': questionForm})

def list(r):

	if not r.user.is_authenticated():
		return redirect('/')

	projects = Project.objects.all().filter(user=r.user)
	return render(r, 'projects/list.html', {'projects' : projects})






