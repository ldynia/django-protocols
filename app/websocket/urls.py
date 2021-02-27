from django.urls import path

from websocket import views


urlpatterns = [
    path('', views.index),
    path('echo/', views.echo),
    path('chat/', views.index),
    path('chat/<str:room_name>/', views.room),
    path('async_chat/<str:room_name>/', views.room),
]