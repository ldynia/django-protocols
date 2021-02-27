"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend.views import index
from websocket import views as ws_view


urlpatterns = [
    path('', index),

    # Views for websocket app
    path('api/ws/echo/', ws_view.echo),
    path('api/ws/chat/', ws_view.index),
    path('api/ws/chat/<str:room_name>/', ws_view.room),
    path('api/ws/async_chat/<str:room_name>/', ws_view.room),

    path('admin/', admin.site.urls),
]
