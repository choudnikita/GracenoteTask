"""
This module can be used to store csv file data into database.
Run below command to execute this:
    python manage.py load_csv_data
"""
from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from Gracenoteapp.models import Teams, GameResults
from pytz import UTC


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the Teams or Game Results data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from Teams.csv and Game_Results.csv into respevtive model"

    def handle(self, *args, **options):
         
        if Teams.objects.exists():
            print('Teams data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        
        if GameResults.objects.exists():
            print('Game results data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        
        print("Creating Teams data")
        for row in DictReader(open('./Teams.csv')):
            try:
                team = Teams()
                team.team_id = row['team_id']
                team.name = row['name']
                team.player_id = row['player_id']
                team.firstname = row['firstname']
                team.lastname = row['lastname']
                raw_birthdate = row['birthdate']
                if raw_birthdate != 'NULL':
                    birthdate = UTC.localize(
                            datetime.strptime(raw_birthdate, DATETIME_FORMAT))
                else:
                    birthdate = None
                team.birthdate = birthdate
                team.save()
            except Exception as ex:
                pass
        
        print("Creating Game_Results data")
        for row in DictReader(open('./Game_Results.csv')):
            try:
                gameresult = GameResults()
                gameresult.league_id = row['league_id']
                gameresult.league_name = row['league_name']
                gameresult.season_id = row['season_id']
                gameresult.season = row['season']
                gameresult.game_id = row['game_id']
                raw_gamedate = row['gamedate']
                if raw_gamedate != 'NULL':
                    gamedate = UTC.localize(
                            datetime.strptime(raw_gamedate, DATETIME_FORMAT))
                else:
                    gamedate = None
                gameresult.gamedate = gamedate
                gameresult.team_id = row['team_id'] #Teams.objects.get(pk=(row['team_id']))
                gameresult.teamname = row['team_name']
                gameresult.goals = row['goals']
                gameresult.penalty = row['penalty']
                gameresult.result = row['result']
                gameresult.save()
            except Exception as ex:
                pass
        
