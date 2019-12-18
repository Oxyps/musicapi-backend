from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404

from .serializers import MusicSerializer
from .pagination import CustomPagination

from .models import Music

class MusicList(generics.ListCreateAPIView): #implementa post e get automaticão
    serializer_class = MusicSerializer
    pagination_class = CustomPagination #teste
    queryset = Music.objects.all()

class MusicDetail(APIView):
    def get_object(self, pk):
        try:
            return Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    # def patch(self, request, pk, format=None):
    #     music = self.get_object(pk)
    #     serializer = MusicSerializer(music, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        music = self.get_object(pk)
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)