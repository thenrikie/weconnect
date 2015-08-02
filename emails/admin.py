from django.contrib import admin
from emails import models
# Register your models here.

class QueueAdmin(admin.ModelAdmin):
	readonly_fields  = ('finished_at', )
	list_display = ('action', 'state', 'item_object', 'item_id','start_at','created_at')

admin.site.register(models.Queue, QueueAdmin)
