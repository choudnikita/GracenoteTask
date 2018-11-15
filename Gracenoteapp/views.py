from rest_framework import serializers, viewsets
from .serializers import TeamSerializer, GameResultSerializer, LeagueDataSerializer
from .models import Teams, GameResults
from rest_framework.response import Response
from collections import OrderedDict

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TeamInfoViewSet(viewsets.ModelViewSet):
    """
    This API returns team details. 
    It accepts team id or team name as query parameters.
    """
    model = Teams
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


    def get_queryset(self):
        # Display None in response until query is posted.
        pass

    def create(self, request, *args, **kwargs):
        # This method gets invoked when query is submitted.
        team_id = request.data.get('team_id')
        teamname = request.data.get('name')
        response_dict = OrderedDict()
        try:
            if team_id:
                queryset = Teams.objects.filter(team_id = team_id)
            elif teamname:
                queryset = Teams.objects.filter(name = teamname)
            else:
                return Response(
                        {'Error' : 'Provide team id or team name to get team information'})
            serializer = TeamSerializer(queryset, many=True)
            if serializer.data:
                # Parsing data to get readable data 
                response_dict['players'] = []
                for elem in serializer.data:
                    for key, val in elem.items():
                        if key == 'team_id' or key == 'name':
                            response_dict[key] = val
                        elif key == 'player_id':
                            response_dict['players'].append({val: 
                                {'firstname': elem['firstname'],
                                'lastname': elem['lastname'],
                                'birthdate': elem['birthdate']}})
                            break
            return Response({'Team Details' : response_dict})
        except Exception as ex:
            logger.error('TeamInfoViewSet failed with exception'.format(str(ex)))
            return Response({'Error': str(ex)})

class LeagueDataViewSet(viewsets.ModelViewSet):
    """
    This API returns league details.
    It accepts league id or league name as query parameters.
    """

    model = GameResults
    queryset = GameResults.objects.all()
    serializer_class = LeagueDataSerializer


    def get_queryset(self):
        # Display None in response until query is posted.
        pass

    def create(self, request, *args, **kwargs):
        # This method gets invoked when query is submitted.
        league_id = request.data.get('league_id')
        league_name = request.data.get('league_name')
        try:
            if league_id:
                queryset = GameResults.objects.filter(league_id=league_id)
            elif league_name:
                queryset = GameResults.objects.filter(league_name=league_name)
            else:
                return Response(
                        {'Error' : 'Provide league id or league name to get league details'})
            serializer = LeagueDataSerializer(queryset, many=True)
            return Response({'League Data' : serializer.data})
        except Exception as ex:
            logger.error('LeagueDataViewSet failed with exception'.format(str(ex)))
            return Response({'Error': str(ex)})
        

class GameResultViewSet(viewsets.ModelViewSet):
    """
    This API returns game results.
    It accepts game id or game date as query parameters.
    """

    model = GameResults
    queryset = GameResults.objects.all()
    serializer_class = GameResultSerializer


    def get_queryset(self):
        # Display None in response until query is posted.
        pass

    def create(self, request, *args, **kwargs):
        # This method gets invoked when query is submitted.
        game_id = request.data.get('game_id')
        gamedate = request.data.get('gamedate')
        try:
            if game_id:
                queryset = GameResults.objects.filter(game_id=game_id)
            elif gamedate:
                queryset = GameResults.objects.filter(gamedate=gamedate)
            else:
                return Response(
                        {'Error' : 'Provide game id or game date to get game results'})
            serializer = GameResultSerializer(queryset, many=True)
            return Response({'Game Results' : serializer.data})
        except Exception as ex:
            logger.error('GameResultViewSet failed with exception'.format(str(ex)))
            return Response({'Error': str(ex)})


