from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from invites.views import *
from votes.views import message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="Home"),
    path('votes/', include('votes.urls')),
    path('message',message,name="Message"),

    url(r'^invite$', invite, name="INVITE RECORDER"),
]
