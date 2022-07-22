from django.db import models


class Group(models.Model):
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.group
