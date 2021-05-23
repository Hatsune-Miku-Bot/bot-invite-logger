from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from invites.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="Home"),

    url(r'^invite$', invite, name="INVITE RECORDER"),
]
