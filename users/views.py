from django.shortcuts import render, redirect
from users.models import UserProfile
from users import forms
from authentication.models import User
from django.db import connection

# Create your views here.

def profile_customer(r):
	form = forms.Customer(initial={'first_name': r.user.first_name, 'last_name': r.user.last_name});
	if (r.method == 'POST'):
		form =  forms.Customer(r.POST);
		if form.is_valid():
			user = User(id=r.user.id)
			user.first_name = r.POST['first_name']
			user.last_name =r.POST['last_name']
			user.save(update_fields=['first_name', 'last_name'])

	return render(r, 'users/profile/customer.html', {'form' : form})

def profile_business(r):

	#whiteListProfile = {k: r.POST.get(k, False) for k in forms.Business.fields}
	form = forms.Business(initial={})
	return render(r, 'users/profile/business.html', {'form' : form})


def profile(r):
	if hasattr(r.user, 'userprofile') and r.user.userprofile.role == 'COMPANY':
		return profile_business(r)
	elif hasattr(r.user, 'userprofile') and r.user.userprofile.role == 'CUSTOMER':
		return profile_customer(r)
	else:
		return redirect('/')
