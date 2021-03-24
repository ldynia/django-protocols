from django.contrib import admin
from django.urls import path
from modernrpc.views import RPCEntryPoint

from frontend.views import index
from rest.views import DummyViewSet
from websocket import views as ws_view

urlpatterns = [
    path('', index),

    # RPC
    path('api/rpc', RPCEntryPoint.as_view()),

    # REST
    path('api/rest/dummie', DummyViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/rest/dummie/<int:id>', DummyViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path('api/rest/dummies', DummyViewSet.as_view({
        'get': 'list'
    })),

    # Views for websocket app
    path('api/ws/echo/', ws_view.echo),
    path('api/ws/chat/', ws_view.index),
    path('api/ws/chat/<str:room_name>/', ws_view.room),
    path('api/ws/async_chat/<str:room_name>/', ws_view.room),

    path('admin/', admin.site.urls),
]
