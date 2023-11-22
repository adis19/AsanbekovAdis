from django.contrib import admin
from .models import GameListModel, Release, Slider

admin.site.register(GameListModel)
admin.site.register(Release)
admin.site.register(Slider)

