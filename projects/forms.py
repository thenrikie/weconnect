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
			kwargs = {
				'label': item.get('question'),
				'queryset': item['queryset']
			}

			if item.get('type') == 'CheckboxSelectMultiple':
				field = forms.ModelMultipleChoiceField
				kwargs['widget'] = forms.CheckboxSelectMultiple

			elif item.get('type') == 'RadioSelect':
				field = forms.ModelChoiceField
				kwargs['widget'] = forms.RadioSelect
				kwargs['empty_label'] = None

			elif item.get('type') == 'Select':
				field = forms.ModelChoiceField
				kwargs['widget'] = forms.Select
				kwargs['empty_label'] = None

			else:
				raise ValueError('Unsupported question type. Must be CheckboxSelectMultiple, RadioSelect or Select')


			self.fields['business_question_' + str(i)] = field(**kwargs)

class Cancel(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['cancelled_reason', 'cancelled_reason_other']
		widgets = {
			'cancelled_reason' : forms.RadioSelect,
			'cancelled_reason_other' : forms.Textarea
		}


class Project(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Project, self).__init__(*args, **kwargs)
		self.fields['my_place'].empty_label = None

 
	class Meta:
		model = Project
		fields = ['budget_lower', 'budget_upper', 'urgency', 'can_travel', 'travel_distance', 'company_travel', 'my_place', 'desc']
		widgets = {
			'travel_distance': forms.CheckboxSelectMultiple,
			'desc': forms.Textarea
		}