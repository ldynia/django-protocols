from django.urls import re_path

from websocket.consumers import ChatAsyncConsumer
from websocket.consumers import ChatConsumer
from websocket.consumers import EchoConsumer


websocket_urlpatterns = [
    re_path(r'api/ws/echo/$', EchoConsumer.as_asgi()),
    re_path(r'api/ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    re_path(r'api/ws/async_chat/(?P<room_name>\w+)/$', ChatAsyncConsumer.as_asgi()),
]