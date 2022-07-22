from django.contrib import admin

from examination.models import Examination, ExamQuestions


class ExamQuestionsInLine(admin.TabularInline):
    model = ExamQuestions


class ExaminationAdmin(admin.ModelAdmin):
    inlines = [ExamQuestionsInLine]


admin.site.register(Examination, ExaminationAdmin)