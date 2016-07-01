from django.shortcuts import render
from django.shortcuts import get_object_or_404

from models import Game

# Create your views here.
def game(request, game):
    thegame = get_object_or_404(Game, url=game)
    context = {'game': thegame }
    return render(request, "main.html" , context)
