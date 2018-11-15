'''
This module contains unit testcases to test TeamInfoViewSet,
LeagueDataViewSet, GameResultViewSet.
Use below command to run this -
 ./manage.py test
'''

from django.test import TestCase, RequestFactory
from .views import TeamInfoViewSet, LeagueDataViewSet, GameResultViewSet

import json

class FilterPostDataApiTest(TestCase):
    def setUp(self):
        # Using the standard RequestFactory API to create a form request
        self.factory = RequestFactory()

    def test_TeamInfoViewSet(self):
        '''
        Create an instance of a GET request.
        '''
        request = self.factory.get("/", format='json')
        response = TeamInfoViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_LeagueDataViewSet(self):
        '''
        Create an instance of a GET request.
        '''
        request = self.factory.get("/", format='json')
        response = LeagueDataViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_GameResultViewSet(self):
        '''
        Create an instance of a GET request.
        '''
        request = self.factory.get("/", format='json')
        response = GameResultViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        # Can be used to delete instances
        pass

