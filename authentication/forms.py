from authentication.models import User
from django.forms import ModelForm, PasswordInput

"""
class Login(ModelForm):
	class Meta:
		model = User
		fields = ('email', 'password')
		widgets = {
			'password': PasswordInput()
		}

"""