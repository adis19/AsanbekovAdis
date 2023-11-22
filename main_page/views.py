from django.shortcuts import render, get_object_or_404
from .models import GameListModel, Release, Slider


def game_list_view(request):
    if request.method == "GET":
        games_list = GameListModel.objects.all()
        release_list = Release.objects.all()
        slider_list = Slider.objects.all()
        return render(request, template_name='games/index.html', context={
            'game_list': games_list,
            'release_list': release_list,
            'slider_list': slider_list
        })

#GET ID
def games_list_detail_view(request, id):
    if request.method == 'GET':
        game_id = get_object_or_404(GameListModel, id=id)
        return render(request, template_name='games/games_detail.html', context={'game_id': game_id})