from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(user)

	DISTANCE = (
		()
	)

	#user profile goes here
	role = models.CharField(max_length=25)
	business_name = models.CharField(max_length=256)
	mobile_number = models.CharField(max_length=100)
	website = models.URLField(max_length=512)
	desc = models.CharField(max_length=1024)
	get_sms = models.BooleanField()
	address_1 = models.CharField(max_length=512)
	address_2 = models.CharField(max_length=512)
	address_3 = models.CharField(max_length=512)
	address_4 = models.CharField(max_length=512)

	can_travel = models.BooleanField()
	travel_distance = models.CharField(max_length=25)

