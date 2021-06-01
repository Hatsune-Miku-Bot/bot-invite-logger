import ast
import json

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
    if request.META['HTTP_AUTHORIZATION'] or request.headers.get('Authorization') == settings.PASSWORD:
        userid = json.loads(request.body.decode("utf-8")).get('user')
        message_me(int(userid), 'Top.GG')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def discordbotlist(request):
    if request.META.get('HTTP_AUTHORIZATION') or request.headers.get('Authorization') == settings.PASSWORD:
        userid = json.loads(request.body.decode("utf-8")).get('id')
        message_me(int(userid), 'Discord Bot List')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def discordboats(request):
    if request.META['HTTP_AUTHORIZATION'] or request.headers.get('Authorization') == settings.PASSWORD:
        try:
            userid = ast.literal_eval(request.body.decode("utf-8")).get('user').get('id')
        except:
            userid = json.loads(request.body.decode("utf-8")).get('user').get('id')
        message_me(int(userid), 'Discord Boats')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def botsfordiscord(request):
    if request.META['HTTP_AUTHORIZATION'] or request.headers.get('Authorization') == settings.PASSWORD:
        userid = request.POST.get('user') or ast.literal_eval(request.body.decode("utf-8")).get('user')
        message_me(int(userid), 'Bots For Discord')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def discordlistspace(request):
    if request.META['HTTP_AUTHORIZATION'] or request.headers.get('Authorization') == settings.TOKEN:
        userid = ast.literal_eval(request.body.decode("utf-8")).get('user').get('id')
        message_me(int(userid), 'Discordlist Space')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def fateslist(request):
    if request.META['HTTP_AUTHORIZATION'] or request.headers.get('Authorization') == settings.PASSWORD:
        userid = json.loads(request.body.decode("utf-8")).get('id')
        message_me(int(userid), 'Fates List')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def bladebotlist(request):
    if request.META.get('HTTP_AUTHORIZATION') or request.headers.get('Authorization') or request.headers.get('Password') or request.headers.get('password') == settings.PASSWORD:
        try:
            userid = request.POST.get('userid') or ast.literal_eval(request.body.decode("utf-8")).get('userid')
        except:
            userid = json.loads(request.body.decode("utf-8")).get('userid')
        message_me(int(userid), 'Blade Bot List')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_POST
def voidbots(request):
    if request.META['HTTP_AUTHORIZATION'] or request.headers.get('Authorization') == settings.PASSWORD:
        userid = request.POST.get('user')  or ast.literal_eval(request.body.decode("utf-8")).get('user')
        message_me(int(userid), 'Void Bots')
        return HttpResponse('Thanks')
    else:
        return HttpResponseNotAllowed(['GET','POST'])
