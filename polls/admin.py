from django.contrib import admin

# Register your models here.
from polls.models import Choice, Question
#  class QuestionAdmin(admin.ModelAdmin):
#     list_display = ("question", "choice" "tendency")

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,                {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

