from django.utils import timezone
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
