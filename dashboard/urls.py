from django.urls import  path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.list_game, name='list_games')
]

