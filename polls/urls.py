from django.conf import settings
from django.urls import path
from django.conf.urls import include
from django.views.static import serve

from . import views
from polls.views import HomeView, HighscoreView, rate, quote

urlpatterns = [
    path('home', HomeView),
    path('highscore', HighscoreView),
    path('rating/<int:candidate_id>/<int:rating>', rate),
    path('quote/<int:candidate_id>', quote),
]


