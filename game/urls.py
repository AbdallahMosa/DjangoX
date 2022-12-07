from django.urls import path
from .views import GameListView,GameDetailView,GameCreateView ,GameUpdateView,GameDeleteView
urlpatterns = [
    path('game/',GameListView.as_view(),name ='game_list'),
    path('game/<int:pk>/',GameDetailView.as_view(), name='game_detail'),
    path('game/create/',GameCreateView.as_view(), name='game_create'),
    path('game/update/<int:pk>',GameUpdateView.as_view(), name='game_update'),
    path('game/delete/<int:pk>',GameDeleteView.as_view(), name='game_delete'),
]