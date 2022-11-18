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

class Workout (models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

class Goal (models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    completion_status = models.BooleanField(default=False)
    category = models.CharField(max_length=10)
    start_status = models.FloatField()
    current_status = models.FloatField()
    target_status = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


