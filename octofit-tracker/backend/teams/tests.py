from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Challenge

class TeamTestCase(TestCase):
    def setUp(self):
        self.captain = User.objects.create_user(username='captain', password='12345')
        self.team = Team.objects.create(name='Test Team', captain=self.captain)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.captain.username, 'captain')

class ChallengeTestCase(TestCase):
    def setUp(self):
        self.challenge = Challenge.objects.create(
            name='Test Challenge',
            description='A test challenge',
            start_date='2023-01-01',
            end_date='2023-01-31'
        )

    def test_challenge_creation(self):
        self.assertEqual(self.challenge.name, 'Test Challenge')
        self.assertTrue(self.challenge.is_active)
