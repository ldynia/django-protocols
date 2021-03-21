# Description

Simple Django project for demonstrating how to implement and use various network protocols.

# Instructions

```bash
$ docker-compose up
```

# REST API

```bash
$ curl -X GET -s 'http://localhost:8080/api/rest/dummies' | jq
$ curl -X GET -s 'http://localhost:8080/api/rest/dummies/2' | jq
$ curl -X GET -s 'http://localhost:8080/api/rest/dummies?id=1&id=2&id=3' | jq
$ curl -X POST -s 'http://localhost:8080/api/rest/dummies' \
    --form 'day="1"' \
    --form 'weekday="Monday"' \
    --form 'month="January"' \
    --form 'year="1984"' | jq
$ curl -X PUT -s 'http://localhost:8080/api/rest/dummies/11' \
    --form 'day="2"' \
    --form 'weekday="Tuesday"' \
    --form 'month="February"' \
    --form 'year="1985"' | jq
$ curl -X PATCH -s 'http://localhost:8080/api/rest/dummies/11' \
    --form 'year="1984"' | jq
$ curl -X DELETE -I 'http://localhost:8080/api/rest/dummies/11'
```

# Websocket API

```
http://localhost:8080/
http://localhost:8080/api/ws/echo
http://localhost:8080/api/ws/chat
http://localhost:8080/api/ws/async_chat

ws://localhost/api/ws/echo
ws://localhost/api/ws/chat
ws://localhost/api/ws/async_chat
```

# OSI - OPEN SYSTEMS INTERCONECTION

![OSI Model](https://8d00aad6-a-62cb3a1a-s-sites.googlegroups.com/site/yutbms/osi-model-1/osi.gif?attachauth=ANoY7co8YLKo3gGYyDtx5fWANjuyXbDeEno_llnTgWTOBIbVhWJuZXTViFiOJDPVyK5Ja5pfXC6TXiSH8LeeBG1phZzxiW1T8H_jKJopTzFIWhpwczvintD3aJdFA1L4bavN-tG3nJKeJ77P9s-p0_ft6BIEKIK7tX5Dev8AJUdGvgSgXy5j5p0N13DOtkIghiEaGQ7TNJA5dllTTQ9dpt70kKhBgnpQfg%3D%3D&attredirects=0)

![Data Frame](http://ann.logan.tripod.com/Image3.gif)


## Websockets

Links:
* [RFC6455](https://tools.ietf.org/html/rfc6455) Request for Comments
* [Browser Compatibility](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API#browser_compatibility)
* [django-channels](https://channels.readthedocs.io/en/stable/tutorial/index.html) tutorial

![duplex](https://user.oc-static.com/upload/2018/10/03/15385574202102_Pr%C3%A9sentation%20PowerPoint%20-%20Google%20Chrome_2.jpg)

**Handshake - Request**
```
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Origin: http://example.com
```

**Handshake - Response**
```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
```

**Debugging**
```bash
$ docker exec -it django-pro bash
$ watch -n1 ss -s
$ watch -n1 ss -ta
```