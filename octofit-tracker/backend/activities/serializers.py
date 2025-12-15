from rest_framework import serializers
from .models import Activity, Workout

class ActivitySerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_username', 'activity_type', 'duration', 'distance', 'calories', 'points', 'date', 'notes']

class WorkoutSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'user_username', 'name', 'description', 'exercises', 'duration', 'created_at']