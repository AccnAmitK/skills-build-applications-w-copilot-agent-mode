from django.test import TestCase
from django.contrib.auth.models import User
from .models import Activity, Workout

class ActivityTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='running',
            duration=30,
            distance=5.0
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.user.username, 'testuser')
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.points, 60)  # 30 * 2

class WorkoutTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.workout = Workout.objects.create(
            user=self.user,
            name='Morning Run',
            duration=45
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.user.username, 'testuser')
        self.assertEqual(self.workout.name, 'Morning Run')
