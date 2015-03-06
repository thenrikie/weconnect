from django.db import models
from authentication.models import User
from projects.models import Project

# Create your models here.
class Pitch(models.Model):

	RATE = (
		('hourly', 'Hourly Rate'),
		('total', 'Estimated project cost'),
		('NA', 'I do not want to provide a price yet')
	)

	STATE = (
		('waiting', 'Waiting'),
		('accepted', 'Company Accepted'),
		('hired', 'Hired'),
		('rejected', 'Customer rejected')
	)

	project = models.ForeignKey(Project)
	company = models.ForeignKey(User)


	price = models.FloatField(blank=True)
	desc = models.CharField(max_length=1024, blank=True, verbose_name='description')

	rate = models.CharField(max_length=25,
			choices=RATE,
			default='total'
	)

	state = models.CharField(max_length=25, choices=STATE, default='waiting')
	state_changed_at = models.DateTimeField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
	pitch = models.ForeignKey(Pitch)
	sender = models.ForeignKey(User, related_name='sender')
	recipient = models.ForeignKey(User, related_name='recipient')
	content =  models.CharField(max_length=4096)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


def upload_filename(path, model, filename):
	nameparts = filename.split(".")
	return 'messages/' + str(model.id) + '.' + nameparts[len(nameparts) - 1]


class MessageAttachment(models.Model):
	message = models.ForeignKey(Message, related_name='attachment')
	file = models.FileField(upload_to=upload_filename, null=True, blank=True)
