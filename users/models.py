from django.db import models
from authentication.models import User
from  django.core.validators import URLValidator

# Create your models here.
class SubBusiness(models.Model):
	name = models.CharField(max_length=255)
	role = models.CharField(max_length=255, blank=True)
	desc = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.name

	def as_json(self):
		return {
			'name': self.name,
			'id': self.id,
			'business': self.business_set.all().first().id
		}

class Business(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255, blank=True)
	rank = models.IntegerField(default=1)
	sub_business = models.ManyToManyField(SubBusiness)

	def __str__(self):
		return self.name

class District(models.Model):
	text = models.CharField(max_length=512)

	def __str__(self):
		return self.text


def upload_filename(path, model, filename):
	nameparts = filename.split(".")
	return path + str(model.user.id) + '.' + nameparts[len(nameparts) - 1]

def logo_filename(model, filename):
	return upload_filename('logos/companies/', model, filename)

def workimage_filename(model, filename):
	return 'work_images/companies/' + str(model.id) + '/' + filename

def workattach_filename(model, filename):
	return 'work_attachs/companies/' + str(model.id) + '/' + filename


def person_filename(model, filename):
	return upload_filename('photos/people/', model, filename)

class UserProfile(models.Model):

	user = models.OneToOneField(User)
	business = models.ManyToManyField(Business)
	sub_business = models.ManyToManyField(SubBusiness)

	ROLE = (
		('CUSTOMER', 'Customer'),
		('COMPANY', 'Company')
	)

	TRAVEL = (
 		('anywhere', 'Anywhere in Hong Kong'),
 		('some_areas', 'Only some areas in Hong Kong')
	)

	#user profile goes here
	role = models.CharField(max_length=25, choices=ROLE, editable=False)



	business_name = models.CharField(max_length=256, verbose_name='business name')
	mobile_number = models.CharField(max_length=100, blank=True, verbose_name='mobile number')

	urlValidator = URLValidator(schemes=['https', 'http'])
	website = models.CharField(max_length=512, blank=True, validators=[urlValidator])

	desc = models.CharField(max_length=1024, blank=True, verbose_name='About Your Company')
	service_desc = models.CharField(max_length=1024, blank=True, verbose_name='Your Services')

	get_sms = models.BooleanField(default=False, verbose_name='Send me an sms when I receive a job request')
	address_1 = models.CharField(max_length=512, blank=True, verbose_name='Room/Floor/Block')
	address_2 = models.CharField(max_length=512, blank=True, verbose_name='Street/Residential address')
	address_3 = models.CharField(max_length=512, blank=True, verbose_name='')
	address_4 = models.CharField(max_length=512, blank=True, verbose_name='Area')

	#to be removed
	can_travel = models.BooleanField(default=False, verbose_name='I can travel to my customers')
	
	travel_to_customer = models.CharField(
		max_length=25, 
		verbose_name='I can travel to my customers',
		choices=TRAVEL,
		default='anywhere'
	)

	travel_distance = models.ManyToManyField(District, related_name='userprofile_travel_distance_set', verbose_name='How far will you travel', blank=True)
	
	only_remote = models.BooleanField(default=False, verbose_name='Only internet or phone')
	
	customer_travel = models.BooleanField(default=False, verbose_name='My customer usually travel to me')

	employees = models.IntegerField(verbose_name='Employees number', default=0)

	business_since = models.CharField(max_length=255, verbose_name='Business since', null=True)

	facebook = models.CharField(max_length=255, blank=True, default='')
	linkedin = models.CharField(max_length=255, blank=True, default='')
	twitter = models.CharField(max_length=255, blank=True, default='')
	pinterest = models.CharField(max_length=255, blank=True, default='')
	instagram = models.CharField(max_length=255, blank=True, default='')
	google = models.CharField(max_length=255, blank=True, default='')

	photo = models.ImageField(upload_to=person_filename, null=True, blank=True)
	logo = models.ImageField(upload_to=logo_filename, null=True, blank=True)

	work_image_1  = models.ImageField(upload_to=workimage_filename, null=True, blank=True)
	work_image_2  = models.ImageField(upload_to=workimage_filename, null=True, blank=True)
	work_image_3  = models.ImageField(upload_to=workimage_filename, null=True, blank=True)

	work_attach_1  = models.FileField(upload_to=workattach_filename, null=True, blank=True)
	work_attach_2  = models.FileField(upload_to=workattach_filename, null=True, blank=True)
	work_attach_3  = models.FileField(upload_to=workattach_filename, null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def is_customer(self):
		return self.role == 'CUSTOMER'

	def is_company(self):
		return self.role == 'COMPANY'

	def unread_message_count(self):
		from pitches.models import Message
		return Message.objects.filter(recipient=self.user, read=False).count();

	def travel_to_customer_text(self):
		for i in self.TRAVEL:
			if i[0] == self.travel_to_customer:
				return i[1]


	def __str__(self):
		return self.user.email

