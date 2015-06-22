from django.shortcuts import render, redirect, get_object_or_404
from users.models import UserProfile
from users import forms
from authentication.models import User
from django.db import connection
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
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
	form_credential = forms.Credential(r.POST or None, instance=r.user)
	form_business_head = forms.BusinessHead(r.POST or None, r.FILES or None, instance=r.user.userprofile)
	form_business_company_desc = forms.BusinessCompanyDesc(r.POST or None, instance=r.user.userprofile)
	form_business_service_desc = forms.BusinessSerivceDesc(r.POST or None, instance=r.user.userprofile)
	form_business_preference = forms.BusinessPreference(r.POST or None, instance=r.user.userprofile)
	form_business_company_detail = forms.BusinessCompanyDetail(r.POST or None, instance=r.user.userprofile)
	form_business_company_social = forms.BusinessCompanySocial(r.POST or None, instance=r.user.userprofile)
	form_business_work = forms.BusinessWorkImage(r.POST or None, r.FILES or None, instance=r.user.userprofile)

	view_values = {
	#	'form' : form, 
		'userprofile' : r.user.userprofile,
		'form_credential' : form_credential,
		'form_business_head': form_business_head,
		'form_business_company_desc' : form_business_company_desc,
		'form_business_service_desc' : form_business_service_desc,
		'form_business_preference' : form_business_preference,
		'form_business_company_detail' : form_business_company_detail,
		'form_business_company_social' : form_business_company_social,
		'form_business_work' : form_business_work
	}

	part = {
		'head' : {'forms' : [form_business_head, form_credential], 'error' : 'form_business_head_error'},
		'company_desc': {'forms' : [form_business_company_desc], 'error' : 'form_business_company_desc_error'},
		'service_desc': {'forms' : [form_business_service_desc], 'error' : 'form_business_service_desc_error'},
		'preference' : {'forms' : [form_business_preference], 'error' : 'form_business_preference_error'},
		'company_detail' : {'forms' : [form_business_company_detail], 'error' : 'form_business_company_detail_error'},
		'company_social' : {'forms' : [form_business_company_social], 'error' : 'form_business_company_social_error'},
		'work' : {'forms' : [form_business_work], 'error': 'form_business_work_error'}
	}

	if r.method == 'POST':

		if r.POST.get('part'):
			
			part_forms = part[r.POST.get('part')]['forms']
			part_form_error = part[r.POST.get('part')]['error']

			allFormValid = True

			for form in part_forms:
				allFormValid = allFormValid and form.is_valid() 

			if allFormValid:
				for form in part_forms:
					form.save()
				return redirect('users:profile')
			else:
				view_values[part_form_error] = True

#		else:
#			form = forms.Business(r.POST, r.FILES, instance=r.user.userprofile)
#			if form.is_valid():
#				form.save()
#				return HttpResponseRedirect(reverse('users:profile'))

	return render(r, 'users/profile/business.html', view_values)

@login_required
def profile(r):
	if hasattr(r.user, 'userprofile') and r.user.userprofile.role == 'COMPANY':
		return profile_business(r)
	elif hasattr(r.user, 'userprofile') and r.user.userprofile.role == 'CUSTOMER':
		return profile_customer(r)
	else:
		return redirect('/')

@login_required
def pub_profile(r, company_id):
	user = get_object_or_404(User, uniqid=company_id)
	if user.userprofile.role != 'COMPANY':
		return redirect('/')

	return render(r, 'users/profile/business_pub.html', {'userprofile' : user.userprofile})
