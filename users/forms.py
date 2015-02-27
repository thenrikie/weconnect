from authentication.models import User
from users.models import UserProfile, Business
from django.forms import ModelForm, PasswordInput, Textarea


class Customer(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

		
class Business(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['business_name', 'website', 'mobile_number', 'desc', 'get_sms',
		 'address_1', 'address_2', 'address_3', 'address_4',
		 'can_travel', 'travel_distance', 'customer_travel', 'only_remote',
		 'employees','facebook', 'linkedin', 'twitter', 'pinterest', 'instagram'
		]
		widgets = {
			'desc': Textarea()
		}
