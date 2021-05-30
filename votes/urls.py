from django.urls import path

from .views import *

urlpatterns = [
    path('topgg/', topgg, name="Top.GG"),
    path('discordbotlist/', discordbotlist, name="Discord Bot List"),
    path('discordboats/',discordboats, name="Discord Boats"),
    path('botsfordiscord/', botsfordiscord, name="Bots For Discord"),
    path('discordlistspace/', discordlistspace, name="Discordlist Space"),
    path('fateslist/', fateslist, name="Fates List"),
    path('bladebotlist/', bladebotlist, name="Blade Bot List"),
    path('voidbots/',voidbots, name="Void Bots")
]
