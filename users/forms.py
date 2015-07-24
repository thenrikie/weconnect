from authentication.models import User
from users.models import UserProfile, Business, SubBusiness
from django.forms import ModelForm, PasswordInput, Textarea, CheckboxSelectMultiple
from django import forms


class Credential(ModelForm):
	class Meta:
		model = User
		fields = ['first_name']


class Customer(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['photo', 'desc']
		widgets = {
			'desc': Textarea()
		}
		
class Business(ModelForm):

	def __init__(self, *args, **kwargs):
		super(Business, self).__init__(*args, **kwargs)
		self.fields['address_area'].empty_label = 'Please select'

	class Meta:
		model = UserProfile
		fields = ['business_name', 'website', 'mobile_number', 'desc', 'get_sms',
		 'address_1', 'address_2', 'address_3', 'address_area',
		 'can_travel', 'travel_distance', 'customer_travel', 'only_remote',
		 'employees','facebook', 'linkedin', 'twitter', 'pinterest', 'instagram','logo', 'photo'
		]
		widgets = {
			'travel_distance': CheckboxSelectMultiple,
			'desc': Textarea
		}

class BusinessHead(ModelForm):

	def __init__(self, *args, **kwargs):
		super(BusinessHead, self).__init__(*args, **kwargs)
		self.fields['address_area'].empty_label = 'Please select'
		
	class Meta:
		model = UserProfile
		fields = [
			'business_name', 
			'website', 
			'mobile_number', 
			'photo', 
			'address_1', 
			'address_2', 
			'address_3', 
			'address_area',
			'employees',
			'business_since',
			'logo'
		]

class BusinessCompanyDesc(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['desc']
		widgets = {
			'desc': Textarea
		}

class BusinessSerivceDesc(ModelForm):
	def __init__(self, *args,**kwargs):
		super (BusinessSerivceDesc, self).__init__(*args,**kwargs) # populates the post
		self.fields['sub_business'].queryset = SubBusiness.objects.filter(business=self.instance.business.first)


	class Meta:
		model = UserProfile
		fields = ['sub_business','service_desc']
		widgets = {
			'sub_business': CheckboxSelectMultiple,
			'service_desc': Textarea
		}

class BusinessPreference(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['travel_to_customer','customer_travel','travel_distance']
		widgets = {
			'travel_distance': CheckboxSelectMultiple
		}

class BusinessCompanyDetail(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['address_1', 'address_2', 'address_3', 'address_4','employees','business_since']

class BusinessCompanySocial(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['facebook', 'linkedin', 'twitter', 'google', 'pinterest', 'instagram']

class BusinessWorkImage(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['work_image_1', 'work_image_2', 'work_image_3']
		
class ShowCase(forms.Form):

	title = forms.CharField(required=True, max_length=1024, widget=forms.TextInput(attrs={"class":"form-control"}))
	attIds = []
	new_count = 0
	new_field_prefix = "new_"

	def __init__(self, *args, **kwargs):
		attIds = kwargs.pop('attIds')
		new_count = kwargs.pop('new_count', 0)
		self.form_name = kwargs.pop('form_name')

		super(ShowCase, self).__init__(*args, **kwargs)

		self.attIds = attIds
		self.new_count = new_count

		for attId in attIds:
			self._add_field('',str(attId))

		for i in range(new_count):
			self._add_field(self.new_field_prefix, str(i))

	def _add_field(self, prefix, id):
		self.fields[self.form_name + '_' + prefix + 'caption_' + id] = forms.CharField(
			max_length=1024,
			widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Add Caption"}),
			required=False
		)
		self.fields[self.form_name + '_' + prefix + 'file_' + id] = forms.FileField(required=False)

	def get_file_rows(self):
		rows = []
		for attId in self.attIds: 
			rows.append({
				'caption' : self[self.form_name + '_caption_' + str(attId)], 
				'file': self[self.form_name + '_file_' + str(attId)],
				'attId': attId
			})

		for i in range(self.new_count): 
			rows.append({
				'caption' : self[self.form_name + '_' + self.new_field_prefix + 'caption_' + str(i)], 
				'file': self[self.form_name + '_' + self.new_field_prefix + 'file_' + str(i)],
			})

		return rows