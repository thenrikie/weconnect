from django.shortcuts import render, redirect, get_object_or_404
from projects import forms
from projects.models import Project

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
	form = forms.Business();
	return render(r, 'projects/create_project_select_business.html', {'form' : form})

def create_project_select_details(r):

	businessForm = forms.Business(r.POST)
	form = forms.Project(initial={ 'business': r.POST['business']})

	if r.method == 'POST':

		form = forms.Project(r.POST, initial={ 'business': r.POST['business']})
		print(r.POST)
		if businessForm.is_valid() and form.is_valid():
			print('passed')

			whiteListProject = {k: r.POST.get(k, False) for k in (
				'urgency', 
				'can_travel', 
				'travel_distance', 
				'company_travel', 
				'my_place'
				)
			}

			project = Project(user=r.user, **whiteListProject)
			project.save()

			project.business.add(businessForm.cleaned_data['business'])

			for var in form.cleaned_data['sub_business']:
				project.sub_business.add(var)

			
			return redirect('/')
		#print("post not passed")




	return render(r, 'projects/create_project_select_details.html', {'form' : form, 'businessForm' : businessForm})

def list(r):

	if not r.user.is_authenticated():
		return redirect('/')

	projects = Project.objects.all().filter(user=r.user)
	return render(r, 'projects/list.html', {'projects' : projects})


#show project details
def show(r, project_id):
	if not r.user.is_authenticated():
		return redirect('/')

	project = get_object_or_404(Project, pk=project_id);


	if project.user == r.user:
		print('Creator View')
		return show_creator_view(r, project)

	elif project.pitch_set.filter(company=r.user.id):
		print('Company view')
		return show_company_view(r, project)

	else:
		print('No Access to this project')
		return redirect('/')


def show_creator_view(r, project):
	return render(r, 'projects/show_creator.html', {'project': project})

def show_company_view(r, project):
	return render(r, 'projects/show_company.html', {'project': project})
