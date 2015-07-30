from django.db import models

# Create your models here.
class Queue(models.Model):

	item_id = models.IntegerField()
	item_object = models.CharField(max_length=255)
	action = models.CharField(max_length=255)
	start_at = models.DateTimeField()
	before_at = models.DateTimeField()
	finished_at = models.DateTimeField(default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	STATE = (
		('waiting', 'waiting'),
		('processing', 'processing'),
		('finished', 'finished'),
	)

	state = models.CharField(max_length=255,
			choices=STATE,
			default='waiting'
	)
