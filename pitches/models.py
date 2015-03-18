from django.db import models
from authentication.models import User
from projects.models import Project
from datetime import datetime

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
		('rejected', 'Customer rejected'),
		('company_rejected', 'Company rejected'),
	)

	project = models.ForeignKey(Project)
	company = models.ForeignKey(User)

	archived = models.BooleanField(default=False)

	price = models.FloatField(blank=True, null=True)
	desc = models.CharField(max_length=1024, blank=True, verbose_name='description', null=True)

	rate = models.CharField(max_length=25,
			choices=RATE,
			default='total',
			null=True
	)

	state = models.CharField(max_length=25, choices=STATE, default='waiting')
	state_changed_at = models.DateTimeField()

	hired_at = models.DateTimeField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def waiting(self):
		return self.state == 'waiting'

	def quoted(self):
		return self.state == 'accepted' or self.state == 'hired'
		
	def change_state(self, state):
		found = False

		for val in self.STATE:
			if state == val[0]:
				found = True

		if not found:
			raise ValueError('Not a valid state')
		else:
			self.state = state
			self.state_changed_at = datetime.now()
			if self.state == 'hired':
				self.hired_at = datetime.now()

	def company_unread_message_count(self):
		self.message_set.filter(read=False, recipient=self.company, pitch=self).count()

	def customer_unread_message_count(self):
		self.message_set.filter(read=False, recipient=self.project.user, pitch=self).count()

class Message(models.Model):
	pitch = models.ForeignKey(Pitch)
	sender = models.ForeignKey(User, related_name='sender')
	recipient = models.ForeignKey(User, related_name='recipient')
	content =  models.CharField(max_length=4096)
	read = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


def upload_filename(path, model, filename):
	nameparts = filename.split(".")
	return 'messages/' + str(model.id) + '.' + nameparts[len(nameparts) - 1]


class MessageAttachment(models.Model):
	message = models.ForeignKey(Message, related_name='attachment')
	file = models.FileField(upload_to=upload_filename, null=True, blank=True)
