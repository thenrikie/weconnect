from django.contrib import admin
from users import models
# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('text', 'rank')

admin.site.register(models.Business)
admin.site.register(models.SubBusiness)
admin.site.register(models.District, DistrictAdmin)
admin.site.register(models.UserProfile)