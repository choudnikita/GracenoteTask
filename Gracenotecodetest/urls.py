"""Gracenotecodetest URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from Gracenoteapp.views import TeamInfoViewSet, LeagueDataViewSet, GameResultViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'teamdetails', TeamInfoViewSet)
router.register(r'leaguedetails', LeagueDataViewSet, 'leaguedetails')
router.register(r'gameresults', GameResultViewSet, 'gameresults')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]
