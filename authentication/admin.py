from django.contrib import admin

# Register your models here.
from authentication.models import User

class UserAdmin(admin.ModelAdmin):
	readonly_fields  = ('uniqid', )

admin.site.register(User, UserAdmin)