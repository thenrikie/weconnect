from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import redirect
from authentication import forms
from authentication.models import User
from users.models import UserProfile, SubBusiness
import json
from emails import sender

# Create your views here.

def login(r):

	if r.user.is_authenticated():
		return redirect('/')

	if r.method == 'POST':
		form = AuthenticationForm(data=r.POST);
		if form.is_valid():
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
	#redirect if logged in
	if r.user.is_authenticated():
		return redirect('/')
	return render(r, 'auth/register.html')

def create_customer(user_detail):
	# Create user object
	user = User.objects.create_user(
		email=user_detail['email'], 
		first_name=user_detail['first_name'], 
		last_name=user_detail['last_name'], 
		password=user_detail['password']
	);
	
	#Create user profile
	userProfile = UserProfile(role='CUSTOMER', user=user);
	userProfile.save()

	user = auth.authenticate(username=user_detail['email'], password=user_detail['password'])

	return user

def register_customer(r):
	#redirect if logged in
	if r.user.is_authenticated():
		return redirect('/')


	if r.method == 'POST':
		form = forms.Register(r.POST, label_suffix='');
		if form.is_valid():
			user = create_customer(r.POST)
			if user is not None and user.is_active:
				auth.login(r, user)
				sender.signup_customer(user.email, {'name': user.full_name()})
				return redirect('/')

	else:
		form = forms.Register(label_suffix='')

	return render(r, 'auth/register_customer.html', {'form' : form})



def register_business(r):
	#redirect if logged in
	if r.user.is_authenticated():
		return redirect('/')

	form = forms.Register(label_suffix='');

	if r.method == 'POST':
		form = forms.Register(r.POST, label_suffix='')
		if form.is_valid():
			r.session['register_business_user'] = {'email' : r.POST['email'], 'first_name': r.POST['first_name'], 'last_name': r.POST['last_name'], 'password': r.POST['password']}
			return redirect('auth:register_business_details')

	return render(r, 'auth/register_business.html', {'form' : form})


def register_business_details(r):

	if r.user.is_authenticated():
		#redirect if logged in
		return redirect('/')
	elif not r.session.get('register_business_user'):
		#redirect if not from previous page
		return redirect('auth:register_business')

	businessForm = forms.Business(r.POST or None)
	form = forms.RegisterBusiness(r.POST or None, label_suffix='')

	subBusinesses = SubBusiness.objects.all();
	sub_business_json = json.dumps([ob.as_json() for ob in subBusinesses])

	if r.method == 'POST':

		if form.is_valid() and businessForm.is_valid():
			# Create user object
			session_user = r.session.get('register_business_user')
			user = User.objects.create_user(
				email=session_user['email'], 
				first_name=session_user['first_name'], 
				last_name=session_user['last_name'], 
				password=session_user['password']
			)
			
			#Create user profile
			whiteListProfile = {k: r.POST.get(k, False) for k in ('business_name', 'website', 'mobile_number', 'desc', 'get_sms',
	 			'address_1', 'address_2', 'address_3', 'address_4',
				'can_travel', 'customer_travel', 'only_remote')
			}

			userProfile = UserProfile(role='COMPANY', user=user, **whiteListProfile);
			userProfile.save()

			userProfile.business.add(businessForm.cleaned_data['business'])

			for sub_business in r.POST.getlist('sub_business'):
				userProfile.sub_business.add(sub_business)

			for d in form.cleaned_data['travel_distance']:
				userProfile.travel_distance.add(d)

			user = auth.authenticate(username=session_user['email'], password=session_user['password'])

			#clear the saved registion session
			del r.session['register_business_user']
			
			if user is not None and user.is_active:
				auth.login(r, user)
				sender.signup_company(user.email, {'name': user.full_name()})
				return redirect('users:profile')

	return render(r, 'auth/register_business_details.html', {
		'form' : form, 
		'businessForm' : businessForm, 
		'sub_business_json': sub_business_json
	})