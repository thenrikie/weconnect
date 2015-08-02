from django.contrib import admin
from projects.models import Project, Question, QuestionOption

class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionOptionInline,
    ]

    list_filter = ('sub_business', )

class ProjectAdmin(admin.ModelAdmin):
	search_fields = ('user__email', )
	list_display = ('id', 'uniqid', 'email', 'project_type')
	list_filter = ('sub_business',)

	def email(self, obj):
		return obj.user.email

	def project_type(self, obj):
		return obj.sub_business.first().name

admin.site.register(Project, ProjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionOption,)
