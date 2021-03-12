from django.db import models

from .fields import IntegerRangeField

class Player(models.Model):

    FOOT = (
        ('Left', 'Left'),
        ('Rigth', 'Rigth'),
    )

    BEST_POSITION = (
        ('CM', 'CM'),
        ('RM', 'RM'),
        ('CB', 'CB'),
        ('CAM', 'CAM'),
        ('RB', 'RB'),
        ('CDM', 'CDM'),
        ('ST', 'ST'),
        ('LWB', 'LWB'),
        ('LB', 'LB'),
        ('LW', 'LW'),
        ('RWB', 'RWB'),
        ('LM', 'LM'),
        ('GK', 'GK'),
        ('RW', 'RW'),
        ('CF', 'CF'),
    )

    short_name     = models.CharField(max_length=255)
    full_name      = models.CharField(max_length=255)
    country        = models.CharField(max_length=255)
    age            = IntegerRangeField(min_value=0, max_value=100)
    overall_rating = IntegerRangeField(min_value=0, max_value=100)
    potential      = IntegerRangeField(min_value=0, max_value=100)
    club           = models.CharField(max_length=255)
    height         = models.FloatField(default=0.0)
    weight         = models.FloatField(default=0.0)
    foot           = models.CharField(max_length=5, choices=FOOT)
    best_postion   = models.CharField(max_length=3, choices=BEST_POSITION)
    value          = models.FloatField(default=0.0)
    wage           = models.FloatField(default=0.0)
    VIT            = IntegerRangeField(min_value=0, max_value=100)
    TIR            = IntegerRangeField(min_value=0, max_value=100)
    PAS            = IntegerRangeField(min_value=0, max_value=100)
    DRI            = IntegerRangeField(min_value=0, max_value=100)
    DEF            = IntegerRangeField(min_value=0, max_value=100)
    PHY            = IntegerRangeField(min_value=0, max_value=100)
    country_code   = models.CharField(max_length=2)

    class Meta:
        ordering = ['-overall_rating', 'potential']

    def __str__(self):
        return self.full_name