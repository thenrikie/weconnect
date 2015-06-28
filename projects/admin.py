from django.contrib import admin
from projects.models import Project, Question, QuestionOption

class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionOptionInline,
    ]

    list_filter = ('sub_business', )

admin.site.register(Project)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionOption)
