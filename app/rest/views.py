from django.http import Http404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

from rest.models import Dummy
from rest.serializers import DummySerializer


def get(id=None):
    if type(id) == list:
        return Dummy.objects.filter(id__in=id)

    if type(id) == int or type(id) == str:
        try:
            return Dummy.objects.get(id=id)
        except Dummy.DoesNotExist:
            raise Http404

    return Dummy.objects.all()


class DummyViewSet(ViewSet):

    def read(self, request, id=None):
        if id:
            dummies = get(id)
            serializer = DummySerializer(dummies)

        if not id and 'id' not in request.query_params:
            dummies = get()
            serializer = DummySerializer(dummies, many=True)

        if not id and 'id' in request.query_params:
            dummies = get(id=request.query_params.getlist('id'))
            serializer = DummySerializer(dummies, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = DummySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def update(self, request, id=None):
        dummy = get(id)
        serializer = DummySerializer(dummy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        dummy = get(id)
        serializer = DummySerializer(dummy, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        dummy = get(id)
        dummy.delete()

        return Response(status=HTTP_204_NO_CONTENT)
