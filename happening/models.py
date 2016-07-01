from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    name = models.CharField(max_length=100)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    dow  = models.IntegerField(choices=DAYS_OF_WEEK, null=True)
    time = models.TimeField(null=True)
    happening = models.BooleanField(default=True)
