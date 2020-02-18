from django.urls import  path, re_path
from . import views

urlpatterns = [
    path('', views.start_game, name='start_game'),
    path('player_1', views.player_1, name='player1'),
    path('player_2', views.player_2, name='player2'),
    path('create_player', views.create_player, name='create_players'),
    path('game', views.game, name='game'),
    path('logout', views.logout, name='logout'),
    re_path(r'^complete_game/(?P<username>\w+)/$', views.complete_game, name='complete_game'),

]
