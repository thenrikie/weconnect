from authentication.models import User
from users.models import UserProfile, Business
from django.forms import ModelForm, PasswordInput, Textarea

"""
class Login(ModelForm):
	class Meta:
		model = User
		fields = ('email', 'password')
		widgets = {
			'password': PasswordInput()
		}

"""

class Register(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password']
		widgets = {
			'password': PasswordInput()
		}

class RegisterBusiness(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['business_name', 'website', 'mobile_number', 'desc', 'get_sms',
		 'address_1', 'address_2', 'address_3', 'address_4',
		 'can_travel', 'travel_distance', 'customer_travel', 'only_remote'
		]
		widgets = {
			'desc': Textarea

		}
