from django.contrib import admin
from interview.models import Interview
from question.admin import QuestionInline


class InterviewAdmin(admin.ModelAdmin):
    readonly_fields = ('date_start',)
    inlines = [QuestionInline]


admin.site.register(Interview, InterviewAdmin)

