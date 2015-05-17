from authentication.models import User
from users.models import UserProfile, Business
from django.forms import ModelForm, PasswordInput, Textarea, CheckboxSelectMultiple
from django import forms

"""
class Login(ModelForm):
	class Meta:
		model = User
		fields = ('email', 'password')
		widgets = {
			'password': PasswordInput()
		}

"""
password_min_length = 6

class Register(ModelForm):
	def __init__(self, *args, **kwargs):
		super(Register, self).__init__(*args, **kwargs)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password']
		widgets = {
			'password': PasswordInput()
		}

	def clean_password(self):
		password = self.cleaned_data.get('password', '')
		if len(password) < password_min_length:
			raise forms.ValidationError("Password must have at least %i characters" % password_min_length)
		else:
			return password

class Business(forms.Form):
	business = forms.ModelChoiceField(queryset=Business.objects.all(), empty_label='')
	
class RegisterBusiness(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['business_name', 'website', 'mobile_number', 'desc', 'get_sms',
		 'address_1', 'address_2', 'address_3', 'address_4',
		 'can_travel', 'travel_distance', 'customer_travel', 'only_remote'
		]
		widgets = {
			'travel_distance': CheckboxSelectMultiple,
			'desc': Textarea
		}
