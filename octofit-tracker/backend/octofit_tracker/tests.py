from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpass123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        # Requires a user
        user = User.objects.create_user(username='a', email='a@a.com', password='pass')
        url = reverse('activity-list')
        data = {'user': user.id, 'type': 'run', 'duration': 30, 'distance': 5.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        user = User.objects.create_user(username='b', email='b@b.com', password='pass')
        url = reverse('workout-list')
        data = {'user': user.id, 'name': 'Morning Cardio', 'description': 'Cardio session', 'duration': 45}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Winners')
        url = reverse('leaderboard-list')
        data = {'team': team.id, 'points': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
