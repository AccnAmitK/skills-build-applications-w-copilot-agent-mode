from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('walking', 'Walking'),
        ('cycling', 'Cycling'),
        ('strength', 'Strength Training'),
        ('swimming', 'Swimming'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.IntegerField(help_text="Duration in minutes")
    distance = models.FloatField(null=True, blank=True, help_text="Distance in km")
    calories = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

    def save(self, *args, **kwargs):
        # Calculate points based on activity
        if self.activity_type == 'running':
            self.points = int(self.duration * 2)  # example: 2 points per minute
        elif self.activity_type == 'walking':
            self.points = int(self.duration * 1)
        elif self.activity_type == 'strength':
            self.points = int(self.duration * 1.5)
        else:
            self.points = int(self.duration * 1)
        super().save(*args, **kwargs)


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    exercises = models.JSONField(default=list, help_text="List of exercises")
    duration = models.IntegerField(help_text="Estimated duration in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
