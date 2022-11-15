from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    middle_initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=20)

class ActivityLog(models.Model):
    description = models.TextField(blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    time = models.DurationField()
    weight = models.FloatField(blank=True)
    reps = models.IntegerField(blank=True)
    distance = models.FloatField(blank=True)