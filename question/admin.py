from django.contrib import admin
from question.models import Question, QuestionOption


class OptionInline(admin.TabularInline):
    model = QuestionOption
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


admin.site.register(Question, QuestionAdmin)


class QuestionInline(admin.TabularInline):
    model = Question
