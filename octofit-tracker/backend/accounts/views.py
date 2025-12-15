from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@api_view(['GET'])
def leaderboard(request):
    profiles = Profile.objects.order_by('-total_points')[:10]
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
