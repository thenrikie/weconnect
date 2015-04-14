from django.db import models

# Create your models here.
class Contact(models.Model):
	email = models.EmailField(max_length=255, unique=True, verbose_name='Email address')
	name =  models.CharField(max_length=255, verbose_name='business name', blank=True)

	def __str__(self):
		return self.email