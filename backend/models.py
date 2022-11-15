from django.db import models

# Create your models here.

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


