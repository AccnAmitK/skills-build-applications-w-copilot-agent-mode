from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    captain = models.ForeignKey(User, on_delete=models.CASCADE, related_name='captained_teams')
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    max_members = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    @property
    def total_points(self):
        return sum(member.profile.total_points for member in self.members.all() if hasattr(member, 'profile'))

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    teams = models.ManyToManyField(Team, blank=True)
    individual_participants = models.ManyToManyField(User, blank=True, related_name='challenges')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
