from django.db import models
from django.contrib.auth import get_user_model

from quizzes.models import Quiz, Question, Answer

User = get_user_model()


class Examination(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    grade = models.IntegerField(default=100)
    question_grade = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.pk} - {self.person} {self.quiz}"


class ExamQuestions(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE,
                               null=True, blank=True)
    quiz = models.ForeignKey(Examination, on_delete=models.CASCADE,
                             null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, related_name='exam_answer',
                               blank=True, null=True)
    grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.quiz
