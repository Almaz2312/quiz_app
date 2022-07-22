from django.contrib import admin
from .models import Quiz, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    max_num = 4
    min_num = 4
    can_delete = False


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)
