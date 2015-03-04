from django.db import models
from users.models import SubBusiness, Business
from authentication.models import User


# Create your models here.
class Project(models.Model):

	business = models.ManyToManyField(Business)
	sub_business = models.ManyToManyField(SubBusiness)

	user = models.ForeignKey(User)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	