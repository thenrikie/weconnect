from django.contrib import admin
from users import models
# Register your models here.
admin.site.register(models.Business)
admin.site.register(models.SubBusiness)
admin.site.register(models.District)
admin.site.register(models.UserProfile)