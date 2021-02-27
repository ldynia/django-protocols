from django.shortcuts import render


def echo(request):
    return render(request, 'echo.html')


def index(request):
    return render(request, 'index.html')


def room(request, room_name):
    return render(request, 'room.html', {'room_name': room_name})
