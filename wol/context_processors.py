# context_processors.py
from datas.models import *


def common_context(request):
    games = Game.objects.all()
    tab = []
    for i in games:
        temp = {}
        temp['name'] = i.name
        temp['category'] = CatAndGames.objects.filter(game__name=i.name).all()
        tab.append(temp)
    common_data = {
        'catandgames': tab
    }
    return common_data

