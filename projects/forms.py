from authentication.models import User
from users.models import Business, SubBusiness
from projects.models import Project
from pitches.models import Pitch
from django import forms


class BusinessIndex(forms.Form):
	business = forms.ModelChoiceField(queryset=Business.objects.all().order_by('rank'), empty_label='What\'s your business?')

class Business(forms.Form):
	business = forms.ModelChoiceField(queryset=Business.objects.all().order_by('rank'), empty_label='What are you looking for?')

class ProjectQuestion(forms.Form):
	def __init__(self, *args, **kwargs):
		extra = kwargs.pop('extra')
		super(ProjectQuestion, self).__init__(*args, **kwargs)

		for item in extra:
			self.fields[item.get('question').field_name()] = item.get('question').make_field(item.get('required', True))
			
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
		self.fields['my_place'].empty_label = 'Please select'
		if args[0] and args[0].get('urgency') == 'specific':
			self.fields['specific_date'].required = True
		
	
	class Meta:
		model = Project
		fields = [
			'budget_lower', 
			'budget_upper', 
			'urgency', 
			'specific_date', 
			'travel_to_pro', 
			'travel_distance', 
			'my_place', 
			'desc'
		]

		widgets = {
			'travel_distance': forms.CheckboxSelectMultiple,
			'desc': forms.Textarea
		}