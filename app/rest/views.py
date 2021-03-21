from django.http import Http404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest.models import Dummy
from rest.serializers import DummySerializer


def get_objects(id=None):
    if type(id) == int or type(id) == str :
        try:
            return Dummy.objects.get(id=id)
        except Dummy.DoesNotExist:
            raise Http404
    elif type(id) == list:
        return Dummy.objects.filter(id__in=id)
    else:
        return Dummy.objects.all()

# /api/rest/dummie/id
class DummyItem(APIView):

    def get(self, request, id, format=None):
        dummy = get_objects(id)
        serializer = DummySerializer(dummy)

        return Response(serializer.data)

    def put(self, request, id, format=None):
        dummy = get_objects(id)
        serializer = DummySerializer(dummy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        dummy = get_objects(id)
        serializer = DummySerializer(dummy, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        dummy = get_objects(id)
        dummy.delete()

        return Response(status=HTTP_204_NO_CONTENT)

# /api/rest/dummies
class DummyItems(APIView):

    def get(self, request, format=None):
        dummy = get_objects()
        if 'id' in request.query_params:
            ids = request.query_params.getlist('id')
            dummy = get_objects(id=ids)

        serializer = DummySerializer(dummy, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DummySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)