from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path("art/",manage_art_view.as_view()),
    path('team-members/', manage_team_member_view.as_view())
]
