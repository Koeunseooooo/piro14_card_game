from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import CardBattle
from django.utils import timezone
# Create your views here.
# Create your views here.

def main(request):
    return render(request, 'game/main.html')

def login(request):
    return render(request, 'game/login.html')

def game_list(request):
    return render(request, 'game/game_list.html')

def game(request):
    return render(request, 'game/game.html')

def game_alone(request):
    return render(request, 'game/game_alone.html')

def game_option(request):
    return render(request, 'game/game_option.html')

def ranking(request):
    return render(request, 'game/ranking.html')


