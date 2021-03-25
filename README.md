# Description

Simple Django project for demonstrating how to implement and use various network protocols.

# OSI - OPEN SYSTEMS INTERCONECTION

![OSI Model](https://8d00aad6-a-62cb3a1a-s-sites.googlegroups.com/site/yutbms/osi-model-1/osi.gif?attachauth=ANoY7co8YLKo3gGYyDtx5fWANjuyXbDeEno_llnTgWTOBIbVhWJuZXTViFiOJDPVyK5Ja5pfXC6TXiSH8LeeBG1phZzxiW1T8H_jKJopTzFIWhpwczvintD3aJdFA1L4bavN-tG3nJKeJ77P9s-p0_ft6BIEKIK7tX5Dev8AJUdGvgSgXy5j5p0N13DOtkIghiEaGQ7TNJA5dllTTQ9dpt70kKhBgnpQfg%3D%3D&attredirects=0)

![Data Frame](http://ann.logan.tripod.com/Image3.gif)

# Instructions

```bash
$ docker-compose up
$ docker exec django-pro python manage.py seed 10
```

# RPC

**FYI:** Procedure is another name of function.

**Resources**:
* [django-modern-rpc](https://pypi.org/project/django-modern-rpc/)
* [RPC vs REST](https://cloud.google.com/blog/products/application-development/rest-vs-rpc-what-problems-are-you-trying-to-solve-with-your-apis)

The Remote Procedure Call is a protocol for information exchange between a client and a server. Transport layer of RPC protocol is HTTP, that usually is encoded by XML or JSON format. It's very **simple** for a programmer **to write a procedure in one program and call it from another**.

The RPC follows **thought processes of a programmer, calling a remote procedure is syntactically (usually) the same as calling a procedure in normal programming language**. The RPC implementations also tend to be efficient because the data that is passed between the client and the server is usually ***binary encoded**.

In the RPC model, **the addressable units are procedures**, and **the entities of the problem domain are hidden behind the procedures**.

Learning an RPC API is very similar to learning a programming library.

```bash
$ ./rpc_client.py
$ chromium rpc_client.html
```

Start [wireshark](https://www.wireshark.org/) as `sudo` and listen to traffick on `br-a85adb74c466` network interface. Follow below instruction to figure out which interface to listen to.

```bash
# Obtain UUID of network
$ docker inspect django-pro --format='{{range .NetworkSettings.Networks}}{{.NetworkID}}{{end}}' | head -c12
a85adb74c466

# Obtain network interface
$ ip a | grep a85adb74c466 | head -n1 | cut -d':' -f 2
br-a85adb74c466
```

#### When to use RPC?

If the goal of your API is to enable communication between **distributed components that you own and control**, and processing **efficiency is a major concern**, then  RPC in general, and gRPC in particular might be excellent choices.

# gRPC

**Resources**:
* [gRPC](https://grpc.io/)
* [gRPC vs REST](https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them)
* [Protocol Buffers](https://developers.google.com/protocol-buffers)
* [tutorial](https://github.com/ldynia/grpc-python-helloworld)


**gRPC** is an open source remote procedure call (RPC) developed at Google in 2015. It uses HTTP/2 for transport and [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol_Buffers) (method of serializing structured data) as the interface description language. It generates cross-platform client and server bindings for many languages.

```bash
$ git clone git@github.com:ldynia/grpc-python-helloworld.git hellogrpc/

$ docker run --rm -it -d --name grpc -w /app -v $PWD/hellogrpc:/app python:3.7 bash
$ docker exec grpc pip install grpcio grpcio-tools

$ code hellogrpc/ &
$ docker exec -it grpc bash
```

Now need to update the gRPC code used by our application to use the new service definition. This regenerates `helloworld_pb2.py` which contains our generated **request** and **response** classes and `helloworld_pb2_grpc.py` which contains our generated **client** and **server** classes.

```bash
$ python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. greeter.proto
$ python server.py &
$ python client.py
```

#### When to use gRPC?

Us it when you have **control over** the technology choices of all **the clients and the server** of your API. Most common usage scenarios include connecting services in a **microservices** style architecture, or **connecting mobile device clients to backend services**.

gRPC's complex use of HTTP/2 makes it impossible to implement a gRPC client in the browser therfore, **a proxy** is required.

# REST API

The HTTP model is the perfect inverse of the RPC model. In the HTTP model, **the addressable units are the entities** themselves and **the behaviors of the system are hidden behind the entities** as side-effects of creating, updating, or deleting them.

#### When to use REST?

If your primary objective is to make your software more malleable by breaking it down into components that are better isolated from each others' assumptions, OR if your purpose is to open up your systems for future integration by 3rd parties (other teams), then focus on HTTP/JSON APIs.

```bash
$ curl -X GET -s 'http://localhost:8080/api/rest/dummies' | jq
$ curl -X GET -s 'http://localhost:8080/api/rest/dummies?id=1&id=2&id=3' | jq
$ curl -X GET -s 'http://localhost:8080/api/rest/dummie/2' | jq
$ curl -X POST -s 'http://localhost:8080/api/rest/dummie' \
    --form 'day="1"' \
    --form 'weekday="Monday"' \
    --form 'month="January"' \
    --form 'year="1984"' | jq
$ curl -X POST -s 'http://localhost:8080/api/rest/dummie' \
    -H "Content-Type: application/json" \
    -d '{"day":2,"weekday":"Tuesday","month":"February","year":"1985"}' | jq
$ curl -X PUT -s 'http://localhost:8080/api/rest/dummie/11' \
    --form 'day="2"' \
    --form 'weekday="Tuesday"' \
    --form 'month="February"' \
    --form 'year="1985"' | jq
$ curl -X PATCH -s 'http://localhost:8080/api/rest/dummie/11' \
    --form 'year="1984"' | jq
$ curl -X PATCH -s 'http://localhost:8080/api/rest/dummie/11' \
    -H "Content-Type: application/json" \
    -d '{"year":"1985"}' | jq
$ curl -X DELETE -I 'http://localhost:8080/api/rest/dummie/11'
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