from django.urls import path
from django.conf.urls import include
from . import views
from polls.views import HomeView, HighscoreView, rate

urlpatterns = [
    path('home', HomeView),
    path('highscore', HighscoreView),
    path('rating/<int:candidate_id>/<int:rating>', rate)
]