from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    bio = models.TextField(blank=True)
    total_points = models.IntegerField(default=0)
    avatar = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
