from django.shortcuts import render, redirect, get_object_or_404
from users.models import UserProfile, ShowCase, ShowCaseAttachment
from users import forms
from authentication.models import User
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse
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
			#user.last_name =r.POST['last_name']
			#save credentials
			user.save(update_fields=['first_name'])
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

	# get show case -> get showcase attachment -> showcase-xxx-id
	business_showcases = []

	showcases = r.user.userprofile.showcase_set.all()

	for showcase in showcases:

		attachments = showcase.attachments.all()
		attIds = []
		showcase_populate = {
			'title': showcase.title
		}

		for a in attachments:
			attIds.append(a.id)
			showcase_populate[str(showcase.id) + '_caption_' + str(a.id)] = a.caption
			showcase_populate[str(showcase.id) + '_file_' + str(a.id)] = a.file 

		business_showcases.append({
			'form': forms.ShowCase(showcase_populate, showcase_populate, attIds=attIds, new_count=0, form_name=str(showcase.id)),
			'showcase': showcase.id
		})

	# attIds=(8, 7)
	# business_showcases.append({
	# 	'form': forms.ShowCase({'99_caption_7': 'Fuck off'}, r.FILES or None, attIds=attIds, new_count=2, form_name="99"),
	# 	'showcase': 99
	# })

	# business_showcases.append({
	# 	'form': forms.ShowCase(r.POST or None, r.FILES or None, attIds=attIds, form_name="1")
	# })

	view_values = {
		'userprofile' : r.user.userprofile,
		'form_credential' : form_credential,
		'form_business_head': form_business_head,
		'form_business_company_desc' : form_business_company_desc,
		'form_business_service_desc' : form_business_service_desc,
		'form_business_preference' : form_business_preference,
		'form_business_company_detail' : form_business_company_detail,
		'form_business_company_social' : form_business_company_social,
		'form_business_work' : form_business_work,
		'business_showcases': business_showcases,
		'form_business_showcase_template': forms.ShowCase(None, None, attIds=[], new_count=1, form_name="___form_name___")
	}


	part = {
		'head' : {'forms' : [form_business_head, form_credential], 'error' : 'form_business_head_error'},
		'company_desc': {'forms' : [form_business_company_desc], 'error' : 'form_business_company_desc_error'},
		'service_desc': {'forms' : [form_business_service_desc], 'error' : 'form_business_service_desc_error'},
		'preference' : {'forms' : [form_business_preference], 'error' : 'form_business_preference_error'},
		'company_detail' : {'forms' : [form_business_company_detail], 'error' : 'form_business_company_detail_error'},
		'company_social' : {'forms' : [form_business_company_social], 'error' : 'form_business_company_social_error'},
		'work' : {'forms' : [], 'error': 'form_business_work_error'}
	}

	if r.method == 'POST':

		

		if r.POST.get('part') == "work":

			form_name = r.POST.get('form_name')
			att_count = int(r.POST.get('new_count'))

			attachments = showcase.attachments.all()

			showcase_form = forms.ShowCase(
				r.POST, 
				r.FILES, 
				attIds=[a.id for a in attachments], 
				new_count=att_count, 
				form_name=r.POST.get('form_name')
			)
			
			if showcase_form.is_valid():
				print('showcase valid!')

				if(r.POST.get('showcase')):
					print('existing showcase')
					showcase = ShowCase.objects.get(id=int(r.POST.get('showcase')))

					if not showcase or showcase.user_profile != r.user.userprofile:
						print('No permission to update showcase id=' + r.POST.get('showcase'))
						return redirect('/')

					showcase.title = showcase_form.cleaned_data['title']

				else:
					print('new showcase')
					showcase = ShowCase(user_profile=r.user.userprofile, title=showcase_form.cleaned_data['title'])

				showcase.save()

				#update existing attachments:
				for att in attachments:
					att.caption = showcase_form.cleaned_data[form_name + '_caption_' + str(att.id)]
					if showcase_form.cleaned_data[form_name + '_file_' + str(att.id)]:
						att.file = showcase_form.cleaned_data[form_name + '_file_' + str(att.id)]

					att.save()

				for i in range(att_count):
					#only save if there is file
					if showcase_form.cleaned_data[form_name + '_new_file_' + str(i)]:
						att = ShowCaseAttachment(
							showcase=showcase, 
							caption=showcase_form.cleaned_data[form_name + '_new_caption_' + str(i)],
							file=showcase_form.cleaned_data[form_name + '_new_file_' + str(i)]
						)

						att.save()

				return redirect('users:profile')

			else:
				print('showcase invalid!')

				part_form_error = part[r.POST.get('part')]['error']
				view_values[part_form_error] = True

		elif r.POST.get('part'):
			
			part_forms = part[r.POST.get('part')]['forms']
			part_form_error = part[r.POST.get('part')]['error']

			allFormValid = True

			for form in part_forms:
				print(form)
				allFormValid = allFormValid and form.is_valid() 

			if allFormValid:
				for form in part_forms:
					form.save()
				return redirect('users:profile')
			else:
				view_values[part_form_error] = True



	return render(r, 'users/profile/business.html', view_values)

@login_required
def delete_showcase(r, showcase_id):

	if r.method == 'POST':
		showcase = get_object_or_404(ShowCase, id=showcase_id)
		if showcase.user_profile != r.user.userprofile:
			return HttpResponse(status=400)

		#delete attachments
		ShowCaseAttachment.objects.filter(showcase=showcase).delete()
		showcase.delete()

		return HttpResponse(status=204)
	else:
		return HttpResponse(status=400)


@login_required
def delete_showcase_attachment(r, showcase_att_id):
	if r.method == 'POST':
		att = get_object_or_404(ShowCaseAttachment, id=showcase_att_id)
		if att.showcase.user_profile != r.user.userprofile:
			return HttpResponse(status=400)

		#delete attachments
		att.delete()

		return HttpResponse(status=204)
	else:
		return HttpResponse(status=400)

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
