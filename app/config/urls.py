from django.contrib import admin
from django.urls import path
from modernrpc.views import RPCEntryPoint

from frontend.views import index
from rest.views import DummyItem
from rest.views import DummyItems
from websocket import views as ws_view

urlpatterns = [
    path('', index),

    # RPC
    path('api/rpc', RPCEntryPoint.as_view()),

    # REST
    path('api/rest/dummies', DummyItems.as_view()),
    path('api/rest/dummies/<int:id>', DummyItem.as_view()),

    # Views for websocket app
    path('api/ws/echo/', ws_view.echo),
    path('api/ws/chat/', ws_view.index),
    path('api/ws/chat/<str:room_name>/', ws_view.room),
    path('api/ws/async_chat/<str:room_name>/', ws_view.room),

    path('admin/', admin.site.urls),
]
