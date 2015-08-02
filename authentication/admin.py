from django.contrib import admin

# Register your models here.
from authentication.models import User
from users.models import UserProfile
from django.core.urlresolvers import reverse

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(admin.ModelAdmin):
	readonly_fields  = ('uniqid', )
	list_filter = ('userprofile__role', 'userprofile__sub_business', 'userprofile__address_area')
	list_display = ('email', 'first_name', 'business_name', 'area', 'nice_profile_page')
	search_fields = ('email', 'first_name')
	inlines = admin.ModelAdmin.inlines + [UserProfileInline,]

	def nice_profile_page(self, obj):

		if obj.is_company:
			return "<a href=\""  +  reverse('users:pub_profile', args=[obj.uniqid]) + "\" target=\"_blank\">See nice profile</a>"
		return None

	nice_profile_page.allow_tags = True

	def area(self, obj):
		return obj.userprofile.address_area

	def business_name(self, obj):
		return obj.userprofile.business_name

admin.site.register(User, UserAdmin)