from django.db import models
from django.utils import timezone

class Teams(models.Model):
    """
    The "Teams" model for team details
    """

    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_id = models.IntegerField()
    name = models.CharField(max_length=100)
    player_id = models.IntegerField(unique=True)
    firstname =  models.CharField(max_length=100)
    lastname =  models.CharField(max_length=100)
    birthdate =  models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name

class GameResults(models.Model):
    """
    The "GameResults" model for Game details
    """

    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_id = models.IntegerField()
    league_id = models.IntegerField()
    league_name = models.CharField(max_length=100)
    season_id = models.IntegerField()
    season = models.CharField(max_length=100)
    game_id = models.IntegerField()
    gamedate =  models.DateTimeField(blank=True,null=True)
    teamname =  models.CharField(max_length=100)
    goals = models.IntegerField()
    penalty = models.CharField(max_length=100)
    result = models.IntegerField()

    def __str__(self):
        return self.teamname




