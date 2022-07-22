from django.db import models
from django.contrib.auth import get_user_model

from examination.models import Examination
from groups.models import Group
from quizzes.models import Quiz

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                              null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL,
                             null=True, blank=True)
    exam = models.ForeignKey(Examination, on_delete=models.SET_NULL,
                             null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.user.email}"
