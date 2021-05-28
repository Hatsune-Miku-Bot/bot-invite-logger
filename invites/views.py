from datetime import datetime

from django.conf import settings
from django.db.models import F
from django.http import (HttpResponse, HttpResponseNotAllowed,
                         HttpResponsePermanentRedirect)
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET

from .discord import request_discord
from .discord.color import Color
from .discord.embeds import Embed
from .discord.meek_moe import meek_api
from .models import *


def message_me(request):
    a = request_discord.discord_api_req(
        '/users/@me/channels',
        'post',
        data={
            'recipient_id': 571889108046184449
        }
    )
    json = a.json()
    embed=Embed(
        title='Thanks for voting me!',
        color=Color.random(),
        description=f'Thanks **{json["recipients"][0]["username"]}{json["recipients"][0]["discriminator"]}** for voting me! :heart: <:45:778253031523090443>',
        timestamp=datetime.utcnow()
    )
    b = request_discord.discord_api_req(
        f'/channels/{a.json()["id"]}/messages',
        'post',
        data={
            'embed':embed.to_dict()
        }
    )
    request_discord.discord_api_req(
        f'/channels/{a.json()["id"]}/messages',
        'post',
        data={
            'embed':meek_api()
        }
    )
    return HttpResponse('Done')


# Create your views here.
@require_GET
def invite(request):
    try:
        sitename = request.GET['sitename']
        password = request.GET['password']
        if password != settings.PASSWORD:
            return HttpResponseNotAllowed(['GET','POST'])
    except:
        return HttpResponseNotAllowed(['GET','POST'])
    
    if 'discord' in request.META.get('HTTP_REFERER','None') or sitename == 'Direct From Bot':
        try:   
            ListingSite.objects.filter(sitename=sitename).update(
                    invites = F('invites')+1
        )
            a=ListingSite.objects.filter(sitename=sitename).get().url
            if a != '' or a != None:
                return HttpResponsePermanentRedirect(a)
            else:
                return HttpResponsePermanentRedirect('https://github.com/Hatsune-Miku-Bot/miku')
        except:
            return HttpResponseNotAllowed(['GET','POST'])
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_GET
def home(request):
    return render(
        request,
        'index.html',
        {
            'DiscordBotsGG':getindividualstats('Discord Bots GG'),
            'DiscordBotList':getindividualstats('Discord Bot List'),
            'DiscordListSpace':getindividualstats('Discord List Space'),
            'BotsForDiscord':getindividualstats('Bots For Discord'),
            'DiscordBoats':getindividualstats('Discord Boats'),
            'SpaceBotList':getindividualstats('Space Bot List'),
            'BladeBotList':getindividualstats('Blade Bot List'),
            'VoidBots':getindividualstats('Void Bots'),
            'FatesList':getindividualstats('FatesList'),
            'Topgg':getindividualstats('Top.gg'),
            'DirectFromBot':getindividualstats('Direct From Bot'),
        }
    )

@require_GET
def get_invite_stats(request):
    return invitestatsfnc()

def invitestatsfnc():
    a=ListingSite.objects.iterator()
    l = [[str(i.sitename), i.invites] for i in a]
    return l

def getindividualstats(name):
    return ListingSite.objects.filter(sitename=name).get().invites
