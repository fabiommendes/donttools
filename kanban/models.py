from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=140)
    ...


class Issue(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    is_active = models.BooleanField()
    status = ... # to-do, doing or done?
    ...
