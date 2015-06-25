from django.db import models
from authentication.models import User
from projects.models import Project
from datetime import datetime
from django.db.models import signals
from emails import sender as emailSender
from uniqid import models as UniqidModel

def generateUniqid():
	return UniqidModel.generateCode(Pitch.objects.filter, 'uniqid')

# Create your models here.
class Pitch(models.Model):

	uniqid = models.CharField(max_length=UniqidModel.LENGTH, editable=False, unique=True, null=True)

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

	price = models.FloatField(blank=True, null=True, verbose_name='Estimated Price')
	desc = models.CharField(
		verbose_name='Tell us why you would be the best person for this project', 
		max_length=1024,
		blank=True, 
		null=True,
		
	)

	rate = models.CharField(max_length=25,
			choices=RATE,
			default='total',
			null=True
	)

	state = models.CharField(max_length=25, choices=STATE, default='waiting')
	state_changed_at = models.DateTimeField()
	accepted_at  = models.DateTimeField(null=True)
	hired_at = models.DateTimeField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'id: ' + str(self.id) + '; company: ' + self.company.email + ' for project: ' + str(self.project.id)

	def save(self, *args, **kwargs):
		if not self.uniqid:
			self.uniqid = generateUniqid()
		super(Pitch, self).save(*args, **kwargs)


	def waiting(self):
		return self.state == 'waiting'

	def quoted(self):
		return self.state == 'accepted' or self.state == 'hired'

	def rejected(self):
		return self.state == 'rejected'
		
	def hired(self):
		return self.state == 'hired'
		
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
			elif self.state == 'accepted':
				self.accepted_at = datetime.now()

	def company_unread_message_count(self):
		return self.message_set.filter(read=False, recipient=self.company, pitch=self).count()

	def customer_unread_message_count(self):
		print('cmessage')
		print(self.project.user);
		return self.message_set.filter(read=False, recipient=self.project.user, pitch=self).count()

def create_pitch(sender, instance, created, **kwargs):
	if created:
		#send email
		pitch = instance;
		emailSender.request_for_service(pitch.company.email,{
			'name': pitch.company.first_name,
			'customer_name': pitch.project.user.first_name,
			'project_type':  pitch.project.sub_business.first(),
			'pitch' : pitch
		})

signals.post_save.connect(create_pitch, sender=Pitch, dispatch_uid="create_new_pitch")

class Message(models.Model):
	pitch = models.ForeignKey(Pitch)
	sender = models.ForeignKey(User, related_name='sender')
	recipient = models.ForeignKey(User, related_name='recipient')
	content =  models.CharField(max_length=4096)
	read = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


def upload_filename(model, filename):
	#nameparts = filename.split(".")
	return 'messages/' + str(model.message.id) + '/' + filename


class MessageAttachment(models.Model):
	message = models.ForeignKey(Message, related_name='attachment')
	file = models.FileField(upload_to=upload_filename, null=True, blank=True)
