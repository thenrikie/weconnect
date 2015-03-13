from django.shortcuts import render, redirect
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
			project.business.add(1);
			project.sub_business.add(r.POST['sub_business'])
			project.save()
			return redirect('/')
		print("post not passed")

	else:
		print("Not post")


	return render(r, 'projects/create_project_select_details.html', {'form' : form, 'businessForm' : businessForm})



