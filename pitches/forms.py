from authentication.models import User
from users.models import Business, SubBusiness
from projects.models import Project
from pitches.models import Pitch, Message
from django import forms


class Accept(forms.ModelForm):


	def __init__(self, *args, **kwargs):
		super(Accept, self).__init__(*args, **kwargs)
		self.fields['desc'].required = True

	class Meta:
		model = Pitch
		fields = ['desc', 'price', 'rate']
		widgets = {
			'desc' : forms.Textarea,
			'rate' : forms.RadioSelect
		}

	def clean(self):
		cleaned_data = super(Accept, self).clean()
		rate = cleaned_data.get('rate')
		price = cleaned_data.get('price')
		if rate != "NA" and price is None:
			self.add_error('price', 'This value is required')


class Message(forms.Form):
	content = forms.CharField(required=True, widget=forms.Textarea)
	file = forms.FileField(required=False)
