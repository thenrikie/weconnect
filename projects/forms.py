from authentication.models import User
from users.models import Business, SubBusiness
from projects.models import Project
from pitches.models import Pitch
from django import forms


class Business(forms.Form):
	business = forms.ModelChoiceField(queryset=Business.objects.all(), empty_label='What are you looking for?')

class ProjectQuestion(forms.Form):
	def __init__(self, *args, **kwargs):
		extra = kwargs.pop('extra')
		super(ProjectQuestion, self).__init__(*args, **kwargs)

		for i, item in enumerate(extra):
			if item.get('type') == 'CheckboxSelectMultiple':
				field = forms.ModelMultipleChoiceField
				widget = forms.CheckboxSelectMultiple

			elif item.get('type') == 'RadioSelect':
				field = forms.ModelChoiceField
				widget = forms.RadioSelect

			elif item.get('type') == 'Select':
				field = forms.ModelChoiceField
				widget = forms.Select

			else:
				raise ValueError('Unsupported question type. Must be CheckboxSelectMultiple, RadioSelect or Select')


			self.fields['business_question_' + str(i)] = field(label=item.get('question'), widget=widget, queryset=item['queryset'])


class Project(forms.ModelForm):

#
#	def __init__(self, *args, **kwargs):
#		super(Project, self).__init__(*args, **kwargs)
#		if 'initial' in kwargs:
#			self.fields['sub_business'].queryset = SubBusiness.objects.filter(business=kwargs['initial']['business'])

	class Meta:
		model = Project
		fields = ['urgency', 'can_travel', 'travel_distance', 'company_travel', 'my_place']
		widgets = {
			'travel_distance': forms.CheckboxSelectMultiple
		}

