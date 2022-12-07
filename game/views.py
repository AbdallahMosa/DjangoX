from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Game
# Create your views here.

class GameListView(ListView):
    template_name = 'game/game_list.html'
    model = Game
    context_object_name="allgame/games"

class GameDetailView(DetailView):
    template_name = 'game/game_detail.html'
    model = Game
class GameCreateView(CreateView):
    template_name = 'game/game_create.html'
    model = Game
    fields=['title','purchaser','description','img_url']
class GameUpdateView(UpdateView):
    template_name = 'game/game_update.html'
    model = Game
    fields=['title','purchaser','description','img_url']
class GameDeleteView(DeleteView):
    template_name = 'game/game_delete.html'
    model = Game
    success_url= reverse_lazy('game_list')