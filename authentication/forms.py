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
		fields = ['email', 'password', 'first_name', 'last_name']
		widgets = {
			'password': PasswordInput()
		}

class RegisterBusiness(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['business_name', 'website', 'mobile_number', 'desc', 'get_sms']
		widgets = {
			'desc': Textarea()
		}
