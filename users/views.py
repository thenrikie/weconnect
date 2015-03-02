from django.shortcuts import render, redirect
from users.models import UserProfile
from users import forms
from authentication.models import User
from django.db import connection
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def profile_customer(r):
	form = forms.Credential(initial={'first_name': r.user.first_name, 'last_name': r.user.last_name})
	profileForm = forms.Customer(instance=r.user.userprofile)

	if (r.method == 'POST'):
		form = forms.Credential(r.POST);
		profileForm = forms.Customer(r.POST, r.FILES, instance=r.user.userprofile)

		if form.is_valid() and profileForm.is_valid():
			user = User(id=r.user.id)
			user.first_name = r.POST['first_name']
			user.last_name =r.POST['last_name']
			#save credentials
			user.save(update_fields=['first_name', 'last_name'])
			#save profile
			profileForm.save()

			return HttpResponseRedirect(reverse('users:profile'))

	return render(r, 'users/profile/customer.html', {'form' : form, 'profileForm' : profileForm})

def profile_business(r):

	form = forms.Business(instance=r.user.userprofile)

	if (r.method == 'POST'):
		#whiteListProfile = {k: r.POST.get(k, None) for k in forms.Business.Meta.fields}
		form = forms.Business(r.POST, r.FILES, instance=r.user.userprofile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('users:profile'))

	return render(r, 'users/profile/business.html', {'form' : form})


def profile(r):
	if hasattr(r.user, 'userprofile') and r.user.userprofile.role == 'COMPANY':
		return profile_business(r)
	elif hasattr(r.user, 'userprofile') and r.user.userprofile.role == 'CUSTOMER':
		return profile_customer(r)
	else:
		return redirect('/')
