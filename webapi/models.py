from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    number = models.IntegerField(unique=True, primary_key=True, null=False, blank=False,
                                 validators=[MaxValueValidator(999), MinValueValidator(1)])
    date = models.DateField()
    time = models.TimeField()
