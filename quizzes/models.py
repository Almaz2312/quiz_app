from django.db import models

from groups.models import Group


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                              blank=True, null=True)
    question_quantity = models.IntegerField(default=0)
    user_quantity = models.IntegerField(default=0)
    grade = models.IntegerField(default=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL,
                             blank=True, null=True, related_name='question')
    question = models.CharField(max_length=260)
    question_photo = models.ImageField(upload_to='question',
                                       blank=True, null=True)
    grade = models.IntegerField(default=100)
    finish_time = models.TimeField()
    question_time = models.TimeField(default='00:00:20')

    def __str__(self):
        return f'{self.quiz} -- {self.question}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question.question} -- {self.answer}'
