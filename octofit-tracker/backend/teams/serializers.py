from rest_framework import serializers
from .models import Team, Challenge

class TeamSerializer(serializers.ModelSerializer):
    captain_username = serializers.CharField(source='captain.username', read_only=True)
    members_usernames = serializers.SerializerMethodField()
    total_points = serializers.ReadOnlyField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'captain', 'captain_username', 'members', 'members_usernames', 'created_at', 'max_members', 'total_points']

    def get_members_usernames(self, obj):
        return [member.username for member in obj.members.all()]

class ChallengeSerializer(serializers.ModelSerializer):
    teams_names = serializers.SerializerMethodField()
    individual_participants_usernames = serializers.SerializerMethodField()

    class Meta:
        model = Challenge
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'teams', 'teams_names', 'individual_participants', 'individual_participants_usernames', 'is_active']

    def get_teams_names(self, obj):
        return [team.name for team in obj.teams.all()]

    def get_individual_participants_usernames(self, obj):
        return [user.username for user in obj.individual_participants.all()]