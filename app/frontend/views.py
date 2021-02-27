import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    now = datetime.datetime.now()
    html = f"<html><body>Django says date is <b>{now}</b></body></html>"

    return HttpResponse(html)