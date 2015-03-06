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

	business = models.ManyToManyField(Business)
	sub_business = models.ManyToManyField(SubBusiness)

	urgency = models.CharField(max_length=25,
			verbose_name='When do you need this service?',
			choices=URGENCY,
			default='flexible'
	)
	deadline = models.DateTimeField()
	user = models.ForeignKey(User)

	budget_lower = models.FloatField(blank=True)
	budget_upper = models.FloatField(blank=True)

	can_travel = models.BooleanField(default=False, verbose_name='I can travel to them')
	company_travel = models.BooleanField(default=False, verbose_name='They travel to me')
	travel_distance = models.CharField(max_length=25,
			verbose_name='How far will you travel',
			choices=DISTANCE,
			default=10
	)

	desc = models.CharField(max_length=1024, blank=True, verbose_name='description')
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

