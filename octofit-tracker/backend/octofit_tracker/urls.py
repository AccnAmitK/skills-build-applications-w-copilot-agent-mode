"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.views import UserViewSet, ProfileViewSet
from activities.views import ActivityViewSet, WorkoutViewSet
from teams.views import TeamViewSet, ChallengeViewSet
import os

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'challenges', ChallengeViewSet)

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Welcome to Octofit Tracker API',
        'endpoints': {
            'users': f'{base_url}/users/',
            'profiles': f'{base_url}/profiles/',
            'activities': f'{base_url}/activities/',
            'workouts': f'{base_url}/workouts/',
            'teams': f'{base_url}/teams/',
            'challenges': f'{base_url}/challenges/',
            'leaderboard': f'{base_url}/accounts/leaderboard/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
    path('accounts/', include('accounts.urls')),
    path('activities/', include('activities.urls')),
    path('teams/', include('teams.urls')),
]
