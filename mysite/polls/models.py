from django.db import models
from django.utils import timezone
import datetime


class SoilCondition(models.Model):
    I_N = models.CharField(max_length=200)
    I_P = models.CharField(max_length=200)
    I_K = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.I_N}, {self.I_P}, {self.I_K}"



class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
