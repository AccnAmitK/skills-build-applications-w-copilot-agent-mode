from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile
from activities.models import Activity
from teams.models import Team, Challenge

class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **options):
        # Create users
        u1 = User.objects.create_user('student1', 'student1@example.com', 'pass123')
        u2 = User.objects.create_user('student2', 'student2@example.com', 'pass123')
        u3 = User.objects.create_user('teacher', 'teacher@example.com', 'pass123')

        # Create activities
        Activity.objects.create(user=u1, activity_type='running', duration=30, distance=5.0)
        Activity.objects.create(user=u1, activity_type='walking', duration=20)
        Activity.objects.create(user=u2, activity_type='cycling', duration=45, distance=10.0)
        Activity.objects.create(user=u2, activity_type='strength', duration=25)

        # Create team
        team = Team.objects.create(name='Fitness Warriors', captain=u1)
        team.members.add(u1, u2)

        # Create challenge
        challenge = Challenge.objects.create(name='Monthly Fitness Challenge', description='Achieve 100 points this month', start_date='2025-12-01', end_date='2025-12-31')
        challenge.teams.add(team)

        self.stdout.write('Database populated with initial data.')