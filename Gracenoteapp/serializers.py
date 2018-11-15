from rest_framework import serializers

from .models import Teams, GameResults

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teams
        fields = ('team_id', 'name', 'player_id', 'firstname', 'lastname', 
                'birthdate')
        read_only_fields = ('player_id', 'firstname', 'lastname', 'birthdate')

class LeagueDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameResults
        fields = ('game_id', 'league_id', 'league_name', 'season_id',
                'season', 'gamedate', 'team_id', 'teamname', 'goals', 
                'penalty', 'result')
        read_only_fields = ('game_id', 'season_id',
                'season', 'gamedate', 'team_id', 'teamname', 'goals',
                'penalty', 'result')

class GameResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameResults
        fields = ('game_id', 'gamedate', 'goals', 'penalty', 'result')
        read_only_fields = ('goals', 'penalty', 'result')

