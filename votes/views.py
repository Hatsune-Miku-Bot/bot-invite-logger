from django.conf import settings
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_POST

from .utils import message_me


# Create your views here.
def message(request):
    if settings.LOCAL:
        message_me(571889108046184449, 'LOCAL')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def topgg(request):
    if request.META['HTTP_AUTHORIZATION'] == settings.PASSWORD:
        userid = request.POST.get('user')
        message_me(userid, 'Top.GG')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def discordbotlist(request):
    if request.META['HTTP_AUTHORIZATION'] == settings.PASSWORD:
        userid = request.POST.get('id')
        message_me(userid, 'Discord Bot List')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def discordboats(request):
    if request.META['HTTP_AUTHORIZATION'] == settings.PASSWORD:
        userid = request.POST.get('user').get('id')
        message_me(userid, 'Discord Boats')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def botsfordiscord(request):
    if request.META['HTTP_AUTHORIZATION'] == settings.PASSWORD:
        userid = request.POST.get('user')
        message_me(userid, 'Bots For Discord')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def discordlistspace(request):
    if request.META['HTTP_AUTHORIZATION'] == settings.PASSWORD:
        userid = request.POST.get('user').get('id')
        message_me(userid, 'Discordlist Space')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def fateslist(request):
    if request.META['HTTP_AUTHORIZATION'] == settings.PASSWORD:
        userid = request.POST.get('id')
        message_me(userid, 'Fates List')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def bladebotlist(request):
    if request.META['HTTP_AUTHORIZATION'] == settings.PASSWORD:
        userid = request.POST.get('userid')
        message_me(userid, 'Blade Bot List')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def voidbots(request):
    if request.META['HTTP_AUTHORIZATION'] == settings.PASSWORD:
        userid = request.POST.get('user')
        message_me(userid, 'Void Bots')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])
