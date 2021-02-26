import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}</body></html>"
    
    return HttpResponse(html)