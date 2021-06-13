from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# class TrackView(RetrieveAPIView):

#     serializer_class = AlbumSerializer
    # def tracklist(request):
    #     tracks = Album.objects.all()
    #     serializer = AlbumSerializer(tracks,many=True)
    #     return Response(serializer.data)


from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlbumSerializer
from .models import Track,Album
from rest_framework import status



# @api_view(['GET'])
# def tracklist(request):
#     tracks = Album.objects.all()
#     serializer = AlbumSerializer(tracks,many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def tracklist(request):
    tracks = Album.objects.all()
    serializer = AlbumSerializer(tracks,many=True,read_only=True)
    return Response(serializer.data)