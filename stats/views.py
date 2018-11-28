# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import User

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})
