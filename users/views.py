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

	# form = forms.Business(instance=r.user.userprofile)
	form_business_head = forms.BusinessHead(r.POST or None, r.FILES or None, instance=r.user.userprofile)
	form_business_company_desc = forms.BusinessCompanyDesc(r.POST or None, instance=r.user.userprofile)
	form_business_service_desc = forms.BusinessSerivceDesc(r.POST or None, instance=r.user.userprofile)
	form_business_preference = forms.BusinessPreference(r.POST or None, instance=r.user.userprofile)
	form_business_company_detail = forms.BusinessCompanyDetail(r.POST or None, instance=r.user.userprofile)
	form_business_company_social = forms.BusinessCompanySocial(r.POST or None, instance=r.user.userprofile)

	view_values = {
	#	'form' : form, 
		'userprofile' : r.user.userprofile,
		'form_business_head': form_business_head,
		'form_business_company_desc' : form_business_company_desc,
		'form_business_service_desc' : form_business_service_desc,
		'form_business_preference' : form_business_preference,
		'form_business_company_detail' : form_business_company_detail,
		'form_business_company_social' : form_business_company_social
	}

	part = {
		'head' : {'form' : form_business_head, 'error' : 'form_business_head_error'},
		'company_desc': {'form' : form_business_company_desc, 'error' : 'form_business_company_desc_error'},
		'service_desc': {'form' : form_business_service_desc, 'error' : 'form_business_service_desc_error'},
		'preference' : {'form' : form_business_preference, 'error' : 'form_business_preference_error'},
		'company_detail' : {'form' : form_business_company_detail, 'error' : 'form_business_company_detail_error'},
		'company_social' : {'form' : form_business_company_social, 'error' : 'form_business_company_social_error'}
	}

	if r.method == 'POST':

		if r.POST.get('part'):
			
			part_form = part[r.POST.get('part')]['form']
			part_form_error = part[r.POST.get('part')]['error']

			if part_form.is_valid():
				part_form.save()
				return redirect('users:profile')
			else:
				view_values[part_form_error] = True

#		else:
#			form = forms.Business(r.POST, r.FILES, instance=r.user.userprofile)
#			if form.is_valid():
#				form.save()
#				return HttpResponseRedirect(reverse('users:profile'))

	return render(r, 'users/profile/business.html', view_values)


def profile(r):
	if hasattr(r.user, 'userprofile') and r.user.userprofile.role == 'COMPANY':
		return profile_business(r)
	elif hasattr(r.user, 'userprofile') and r.user.userprofile.role == 'CUSTOMER':
		return profile_customer(r)
	else:
		return redirect('/')
