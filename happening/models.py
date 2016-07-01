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

    YES_NO = (
        (True, 'Yes'),
        (False, 'No'),
    )

    name = models.CharField("Game name",max_length=100)
    url = models.SlugField("Url: /", max_length=50, unique=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    dow  = models.IntegerField("Day of Week",choices=DAYS_OF_WEEK, null=True)
    time = models.TimeField("Time",null=True)
    happening = models.BooleanField("Is it happening this week?", choices=YES_NO, default=True)
    created_at = models.DateTimeField("Created On", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Last Updated On", auto_now=True, editable=False)

    def __str__(self):
        return self.name
