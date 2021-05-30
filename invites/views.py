from django.conf import settings
from django.db.models import F
from django.http import HttpResponseNotAllowed, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .models import *


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
