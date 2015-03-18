from authentication.models import User
from users.models import Business, SubBusiness
from projects.models import Project
from pitches.models import Pitch
from django import forms


class Accept(forms.ModelForm):

	desc = forms.CharField(required=True, widget=forms.Textarea)
	price = forms.DecimalField(required=True)

	class Meta:
		model = Pitch
		fields = ['desc', 'price', 'rate']
		widgets = {
			'desc' : forms.Textarea,
			'rate' : forms.RadioSelect
		}

