from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import redirect
from authentication import forms
# Create your views here.

def login(r):

	if r.user.is_authenticated():
		return redirect('/')

	if r.method == 'POST':
		form = AuthenticationForm(r.POST);

		user = auth.authenticate(username=r.POST['username'], password=r.POST['password'])
		if user is not None and user.is_active:
			auth.login(r, user)
			return redirect('/')
	else:
		form = AuthenticationForm();
	
	return render(r, 'auth/login.html', {'form' : form})

def logout(r):
	auth.logout(r)
	return redirect('/');

def register(r):
	if r.user.is_authenticated():
		return redirect('/')

	

	if r.method == 'POST':
		form = forms.Register(r.POST, label_suffix='');
		if form.is_valid():
			user = form.save()

	else:
		form = forms.Register(label_suffix='');

	return render(r, 'auth/register.html', {'form' : form})

def register_business(r):

	form = forms.Register({}, label_suffix='');
	businessForm = forms.RegisterBusiness(label_suffix='');
	return render(r, 'auth/register_business.html', {'businessForm' : businessForm, 'form' : form})