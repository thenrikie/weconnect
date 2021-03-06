from django.shortcuts import render, redirect, get_object_or_404
from projects import forms
from pitches.forms import Message as MessageForm
from authentication.forms import Register
from authentication.forms import RegisterCustomerProfile
from authentication.views import create_customer
from projects.models import Project, Question, QuestionOption, QuestionAnswer
from users.models import Business, SubBusiness
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from emails import sender
from django.contrib.auth.decorators import login_required
import json

# Create your views here.


def create(r):
	
	#get question set based on business selected

	extra = []
	extra_other = []

	if r.POST.get('sub_business', None) is not None:
		questions = Question.objects.filter(sub_business=r.POST['sub_business']).order_by('rank')
		for q in questions:

			extra.append({'question': q})
			other_question = q.make_other_question()

			if other_question:
				extra_other.append({'question': other_question, 'required': False})

	formData = r.POST or None
	if r.POST.get('no_validate'):
		formData = None

	#forms
	businessForm = forms.Business(r.POST or None)
	questionForm = forms.ProjectQuestion(formData, extra=extra);
	questionOtherForm = forms.ProjectQuestion(formData, extra=extra_other);
	form = forms.Project(formData)
	registerForm = Register(formData)
	registerCustomerProfileForm = RegisterCustomerProfile(formData)

	loginForm = AuthenticationForm(data=formData)

	subBusinesses = SubBusiness.objects.all();
	sub_business_json = json.dumps([ob.as_json() for ob in subBusinesses])

	#keep track the field with other option
	have_other_fields = []
	if r.POST.get('sub_business', None) is not None:
		for q in questions:
			other_question = q.make_other_question()
			if other_question:
				have_other_fields.append({
					'parent': questionForm[q.field_name()],
					'child_other': questionOtherForm[other_question.field_name()]
				})

	#check if logged in
	loggedIn = False
	if r.user.is_authenticated():
		loggedIn = True

	checkRegister = r.POST.get('auth_mode') == 'register' and registerForm.is_valid() and registerCustomerProfileForm.is_valid()
	checkLogin = r.POST.get('auth_mode') == 'login' and loginForm.is_valid()
	checkAuthCond = loggedIn or checkRegister or checkLogin

	if r.method == 'POST':

		if questionForm.is_valid():
			for key, question_option_set in questionForm.cleaned_data.items():
				try: 
					for question_option in question_option_set:
						if question_option.other:
							#reset the questionOtherForm validation condition
							extra_item = next(item for item in extra_other if item['question'].parent_id == question_option.question.id)
							extra_item['required'] =True
				except TypeError:
					if question_option_set.other:
							#reset the questionOtherForm validation condition
							extra_item = next(item for item in extra_other if item['question'].parent_id == question_option_set.question.id)
							extra_item['required'] =True

			questionOtherForm = forms.ProjectQuestion(formData, extra=extra_other);

		if businessForm.is_valid() and form.is_valid() and questionForm.is_valid() and questionOtherForm.is_valid() and checkAuthCond:
			if not loggedIn:
				if checkRegister:
					print('Not logged in, create user first')
					user = create_customer(r.POST)
					if user is not None and user.is_active:
						auth.login(r, user)
						sender.signup_customer_with_project(user.email, {
							'name': user.full_name(),
							'role': SubBusiness.objects.get(pk=r.POST.get('sub_business')).role
						})
					else:
						return redirect('/')
				elif checkLogin:
					user = auth.authenticate(username=r.POST['username'], password=r.POST['password'])
					if user is not None and user.is_active and user.is_customer:
						auth.login(r, user)
					else:
						return render(r, 'projects/create_project.html', {
							'form' : form, 
							'questionForm': questionForm, 
							'questionOtherForm': questionOtherForm,
							'registerForm': registerForm,
							'loginForm': loginForm,
							'have_other_fields': have_other_fields,
							'auth_mode': r.POST.get('auth_mode', 'login'),
							'auth_error' : 'Only user with customer role can create a project'
						})			

			whiteListProject = {k: r.POST.get(k, None) for k in (
					'budget_lower', 
					'budget_upper', 
					'urgency', 
					'specific_date', 
					'travel_to_pro', 
					'desc'
				)
			}


			project = Project(user=r.user, my_place=form.cleaned_data['my_place'], **whiteListProject)
			project.save()

			project.business.add(businessForm.cleaned_data['business'].id)

			##for var in form.cleaned_data['sub_business']:
			##	project.sub_business.add(var)
			project.sub_business.add(r.POST.get('sub_business'))

			for var in form.cleaned_data['travel_distance']:
				project.travel_distance.add(var)

			#save question option

			# save question option - other - text
			def saveQuestionOtherAnswer(question_option):
				answer = QuestionAnswer(question=question_option.question, text=questionOtherForm.cleaned_data['business_question_other_' + str(question_option.question.id)], project=project)
				answer.save()

			for key, question_option_set in questionForm.cleaned_data.items():
				try: 
					for question_option in question_option_set:
						project.question_option.add(question_option)

						if question_option.other:
							saveQuestionOtherAnswer(question_option)
				except TypeError:
					project.question_option.add(question_option_set)

					if question_option_set.other:
						saveQuestionOtherAnswer(question_option_set)

			#send email to notify admin
			sender.project_created_admin({
				'customer_name': r.user.full_name(),
				'customer_email': r.user.email,
				'project_id': project.id,
				'project_type': project.sub_business.first()
			})

			return redirect('projects:list')

		#print("post not passed")


	return render(r, 'projects/create_project.html', {
		'form' : form, 
		'sub_business_json': sub_business_json,
		'sub_business' : r.POST.get('sub_business'),
		'businessForm': businessForm,
		'questionForm': questionForm, 
		'questionOtherForm': questionOtherForm,
		'have_other_fields': have_other_fields,
		'registerForm': registerForm,
		'registerCustomerProfileForm': registerCustomerProfileForm,
		'loginForm': loginForm,
		'auth_mode': r.POST.get('auth_mode', 'register')
	})

def list_project(r):

	if not r.user.is_authenticated():
		return redirect('/')

	projects = Project.objects.all().filter(user=r.user).order_by('-created_at')
	return render(r, 'projects/list.html', {'projects' : projects})

@login_required
def cancel(r, project_id):

	if r.method != 'POST':
		return redirect('/')

	project = get_object_or_404(Project, uniqid=project_id)
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


		#notify admin
		sender.project_cancel_admin({
			'customer_name': project.user.full_name(),
			'customer_email': project.user.email,
			'project_id': project.id,
			'project_type': project.sub_business.first()
		})
		
		return redirect('projects:list')
	else:
		return redirect('/')