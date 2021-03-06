from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group
from uniqid import models as UniqidModel

# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password=None):

		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			first_name=first_name,
			last_name=last_name
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, last_name, password):

		user = self.create_user(email,
			password=password,
			first_name=first_name,
			last_name=last_name
		)
		user.is_admin = True
		user.save(using=self._db)
		return user

def generateUniqid():
	return UniqidModel.generateCode(User.objects.filter, 'uniqid')

class User(AbstractBaseUser):
	email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
	first_name = models.CharField(max_length=100, verbose_name='First Name')
	last_name = models.CharField(max_length=100, verbose_name='Last Name', blank=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	uniqid = models.CharField(max_length=UniqidModel.LENGTH, editable=False, unique=True, null=True)
	groups = models.ManyToManyField(Group, blank=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def full_name(self):
		return self.first_name + ' ' + self.last_name

	def get_full_name(self):
	    # The user is identified by their email address
	    return self.email

	def get_short_name(self):
	    # The user is identified by their email address
	    return self.email

	def __str__(self):              # __unicode__ on Python 2
		if hasattr(self,'userprofile') and self.userprofile.is_company():
			return self.userprofile.business_name + " <" + self.email + ">"
		else: 
			return self.email

	def save(self, *args, **kwargs):
		if not self.uniqid:
			self.uniqid = generateUniqid()
		super(User, self).save(*args, **kwargs)

	def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    # Simplest possible answer: Yes, always
	    return True

	def has_module_perms(self, app_label):
	    "Does the user have permissions to view the app `app_label`?"
	    # Simplest possible answer: Yes, always
	    return True

	@property
	def is_staff(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.is_admin

	@property
	def is_company(self):
		return self.userprofile.is_company()

	@property
	def is_customer(self):
		return self.userprofile.is_customer()



