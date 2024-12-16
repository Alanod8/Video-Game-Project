from django.shortcuts import render
from .models import Developer, Game

# Create your views here.


def home(request):
    return render(request, 'games/home.html')



def list_game(request):
    games = Game.objects.all()
    data = {'games': games}
    return render(request, 'games/list_games.html', data)