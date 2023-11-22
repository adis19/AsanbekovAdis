from django.urls import path
from .views import game_list_view, games_list_detail_view

urlpatterns = [
    path('game_list/', game_list_view),
    path('game_list/<int:id>/', games_list_detail_view),
]
