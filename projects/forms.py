from authentication.models import User
from users.models import Business, SubBusiness
from projects.models import Project
from pitches.models import Pitch
from django import forms


class Business(forms.Form):
	business = forms.ModelChoiceField(queryset=Business.objects.all(), empty_label='What are you looking for?')

class Project(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Project, self).__init__(*args, **kwargs)
		if 'initial' in kwargs:
			self.fields['sub_business'].queryset = SubBusiness.objects.filter(business=kwargs['initial']['business'])

	class Meta:
		model = Project
		fields = ['sub_business', 'urgency', 'can_travel', 'travel_distance', 'company_travel', 'my_place']
		widgets = {
			'sub_business' : forms.CheckboxSelectMultiple
		}

