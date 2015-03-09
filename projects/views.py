from django.shortcuts import render
from projects import forms

# Create your views here.


def create(r):
	if r.method == 'POST' and r.POST['business']:
		return create_project_select_details(r)
	else:
		return create_project_select_business(r)

def create_project_select_business(r):
	form = forms.Business();
	return render(r, 'projects/create_project_select_business.html', {'form' : form})

def create_project_select_details(r):
	form = forms.Project(initial={ 'business': r.POST['business']})
	return render(r, 'projects/create_project_select_details.html', {'form' : form})



