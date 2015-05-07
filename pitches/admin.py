from django.contrib import admin
from pitches.models import Pitch
from authentication.models import User

class PitchAdmin(admin.ModelAdmin):
	readonly_fields  = ('hired_at',)
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "company":
			kwargs["queryset"] = User.objects.filter(userprofile__role='Company')
		return super(PitchAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Pitch, PitchAdmin)