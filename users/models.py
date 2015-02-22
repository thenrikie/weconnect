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
	business_name = models.CharField(max_length=256)
	mobile_number = models.CharField(max_length=100)
	website = models.URLField(max_length=512)
	desc = models.CharField(max_length=1024)
	get_sms = models.BooleanField(default=False)
	address_1 = models.CharField(max_length=512)
	address_2 = models.CharField(max_length=512)
	address_3 = models.CharField(max_length=512)
	address_4 = models.CharField(max_length=512)

	can_travel = models.BooleanField(default=False)
	travel_distance = models.CharField(max_length=25,
			choices=DISTANCE,
			default=10
	)
	only_remote = models.BooleanField(default=False)
	customer_travel = models.BooleanField(default=False)
	employees = models.IntegerField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user

