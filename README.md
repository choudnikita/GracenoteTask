# GracenoteTask
Test exercise of Gracenote

Source data files  -
 Teams.csv
 Game_Results.csv

Gracenoteapp/management/commands/load_csv_data.py script is used to store data in database (sqlite3).

This application is developed using Django Rest Framework Browsable API to expose below API endpoints - 
 1. TeamInfoViewSet  - Returns team details in JSON format based on query parameters team id or team name.
 2. LeagueDataViewSet - Returns league details in JSON format based on query parameters league id or league name.
 3. GameResultViewSet - Returns game results in JSON format based on query parameters game id or game date.

Query parameters can be posted using Rawdata or HTML form in webpage.

Unit testcases have been added in test.py in Gracenodeapp.

Heroku host service has been used to host this application.

