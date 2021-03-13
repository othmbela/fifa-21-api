from django.db import models

from .fields import IntegerRangeField

class Team(models.Model):
				
    name            = models.CharField(max_length=255, unique=True)
    country         = models.CharField(max_length=255)
    league          = models.CharField(max_length=255)
    overall         = IntegerRangeField(min_value=0, max_value=100)
    attack          = IntegerRangeField(min_value=0, max_value=100)
    midfield        = IntegerRangeField(min_value=0, max_value=100)
    defence         = IntegerRangeField(min_value=0, max_value=100)
    transfer_budget = models.FloatField(default=0.0)
    players         = models.IntegerField()
    hits            = models.FloatField(default=0.0)

    class Meta:
        ordering = ['-overall']

    def __str__(self):
        return self.name