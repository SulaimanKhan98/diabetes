# models.py in one of your apps
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

timezone.now

class DiabetesResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    age = models.FloatField()
    result = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
