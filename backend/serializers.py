from rest_framework import serializers
from .models import User, ActivityLog, Workout, Goal, StatSheet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # put the fields you want to be translated into JSON
        fields = '__all__'

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'

class StatSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatSheet
        fields = '__all__'