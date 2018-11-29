# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse, HttpResponse

from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})


class Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        users = User.objects.all()
        user = users[0]
        labels = user.total_languages_names()
        default = user.total_languages_nums()
        user_data = {
            "labels": labels,
            "default": default,
        }
        return Response(user_data)

