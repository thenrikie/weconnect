from django.db import models
from users.models import SubBusiness, Business
from authentication.models import User


# Create your models here.
class Project(models.Model):

	
	URGENCY = (
		('flexible', 'I can be flexible'),
		('asap', 'As soon as possible'),
		('week', 'Sometime this week'),
		('specific', 'Specific date'),
		('other', 'Other')
	)

	DISTANCE = (
		('10', '10 miles'),
		('15', '15 miles'),
		('20', '20 miles'),
		('30', '30+ miles')
	)

	DISTRICT = (
		('Islands', 'Islands'),
		('Kwai Tsing', 'Kwai Tsing') ,
		('North', 'North'),
		('Sha Tin', 'Sha Tin'),
		('Tai Po', 'Tai Po'),
		('Tsuen Wan', 'Tsuen Wan'),
		('Tuen Mun', 'Tuen Mun'),
		('Yuen Long', 'Yuen Long'),
		('Kowloon City', 'Kowloon City'),
		('Kwun Tong', 'Kwun Tong'),
		('Sham Shui Po', 'Sham Shui Po'),
		('Wong Tai Sin', 'Wong Tai Sin'),
		('Yau Tsim Mong', 'Yau Tsim Mong'),
		('Central & Western', 'Central & Western'),
		('Eastern', 'Eastern'),
		('Southern', 'Southern'),
		('Wan Chai', 'Wan Chai')
	)

	business = models.ManyToManyField(Business)
	sub_business = models.ManyToManyField(SubBusiness)

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
	travel_distance = models.CharField(max_length=25,
			verbose_name='How far will you travel',
			choices=DISTRICT,
			default='Central & Western'
	)

	my_place = models.CharField(max_length=25, verbose_name='', choices=DISTRICT, default='Central & Western')

	desc = models.CharField(max_length=1024, blank=True, verbose_name='description')
	
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

