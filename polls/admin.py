from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']  # reordering the fields


admin.site.register(
    Question,  # model
    QuestionAdmin  # admin class
)
admin.site.register(Choice)
