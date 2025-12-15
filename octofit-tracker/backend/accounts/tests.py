from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, age=25, bio='Test bio')

    def tearDown(self):
        self.profile.delete()
        self.user.delete()

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.age, 25)
        self.assertEqual(self.profile.bio, 'Test bio')
