from django.db import models
from authentication.models import User

# Create your models here.
class SubBusiness(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)

class Business(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	sub_business = models.ManyToManyField(SubBusiness)



class UserProfile(models.Model):

	user = models.OneToOneField(User)
	business = models.ManyToManyField(Business)


	DISTANCE = (
		('10', '10 miles'),
		('15', '15 miles'),
		('20', '20 miles'),
		('30', '30+ miles')
	)

	ROLE = (
		('CUSTOMER', 'Customer'),
		('COMPANY', 'Company')
	)

	#user profile goes here
	role = models.CharField(max_length=25, choices=ROLE, editable=False)
	business_name = models.CharField(max_length=256, verbose_name='business name')
	mobile_number = models.CharField(max_length=100, blank=True, verbose_name='mobile number')
	website = models.URLField(max_length=512, blank=True)
	desc = models.CharField(max_length=1024, blank=True, verbose_name='description')
	get_sms = models.BooleanField(default=False, verbose_name='Send me an sms when I receive a job request')
	address_1 = models.CharField(max_length=512, blank=True, verbose_name='Room/Floor/Block')
	address_2 = models.CharField(max_length=512, blank=True, verbose_name='Street/Residential address')
	address_3 = models.CharField(max_length=512, blank=True, verbose_name='')
	address_4 = models.CharField(max_length=512, blank=True, verbose_name='Area')

	can_travel = models.BooleanField(default=False, verbose_name='I can travel to my customers')
	travel_distance = models.CharField(max_length=25,
			verbose_name='How far will you travel',
			choices=DISTANCE,
			default=10
	)
	only_remote = models.BooleanField(default=False, verbose_name='Only internet or phone')
	customer_travel = models.BooleanField(default=False, verbose_name='My customer usually travel to me')
	employees = models.IntegerField(verbose_name='Employees number', default=0)

	facebook = models.CharField(max_length=255, blank=True, default='')
	linkedin = models.CharField(max_length=255, blank=True, default='')
	twitter = models.CharField(max_length=255, blank=True, default='')
	pinterest = models.CharField(max_length=255, blank=True, default='')
	instagram = models.CharField(max_length=255, blank=True, default='')


	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user

