from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    priority=models.IntegerField()

