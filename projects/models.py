from django.db import models
from users.models import SubBusiness, Business, District
from authentication.models import User


# Create your models here.

class Question(models.Model):
	TYPE = (
		('CheckboxSelectMultiple', 'CheckboxSelectMultiple'),
		('Select', 'Select'),
		('RadioSelect', 'RadioSelect')
	)

	sub_business = models.ForeignKey(SubBusiness)
	type = models.CharField(max_length=25, verbose_name='', choices=TYPE)
	text = models.CharField(max_length=512)

	def __str__(self):
		return self.text


class QuestionOption(models.Model):
	
	question = models.ForeignKey(Question)
	text = models.CharField(max_length=512)

	def __str__(self):
		return self.text

class Project(models.Model):

	
	URGENCY = (
		('flexible', 'I can be flexible'),
		('asap', 'As soon as possible'),
		('week', 'Sometime this week'),
		('specific', 'Specific date'),
		('other', 'Other')
	)

	business = models.ManyToManyField(Business)
	sub_business = models.ManyToManyField(SubBusiness)
	question_option = models.ManyToManyField(QuestionOption)

	urgency = models.CharField(max_length=25,
			verbose_name='When do you need this service?',
			choices=URGENCY,
			default='flexible'
	)
	deadline = models.DateTimeField(null=True)
	user = models.ForeignKey(User)

	budget_lower = models.FloatField(blank=True, null=True)
	budget_upper = models.FloatField(blank=True, null=True)

	can_travel = models.BooleanField(default=False, verbose_name='I can travel to them')
	company_travel = models.BooleanField(default=False, verbose_name='They travel to me')

	travel_distance = models.ManyToManyField(District, related_name='project_travel_distance_set')
	my_place = models.ForeignKey(District, related_name='my_place')

	desc = models.CharField(max_length=1024, blank=True, verbose_name='Anything else they should know')
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def pitch_count(self):
		return self.pitch_set.exclude(state='waiting').count()

	def ready_pitch(self):
		return self.pitch_set.exclude(state='waiting')

	def awarded(self):
		if self.pitch_set.get(state='hired').count() > 0:
			return True
		return False

	def urgency_text(self):
		for u in self.URGENCY:
			if u[0] == self.urgency:
				return u[1]

	def unread_message_count(self):
		from pitches.models import Message
		return Message.objects.filter(read=False, pitch__project=self, recipient=self.user).count()

