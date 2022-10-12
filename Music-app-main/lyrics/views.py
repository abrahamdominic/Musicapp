from django.shortcuts import render
from .models import Lyric
from song.models import Song
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LyricSerializer

# Create your views here.
@api_view(['POST',])
def add_lyric(request,song_id):
    song = Song.objects.get(id=song_id)
    lyric = Lyric(song_id = song)
    serialized_data = LyricSerializer(lyric,data = request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_all_lyrics(request):
    lyrics = Lyric.objects.all()
    serialized_data = [LyricSerializer(lyric).data for lyric in lyrics]
    return Response(serialized_data)

@api_view(['GET',])
def get_a_lyric(request,lyric_id):
    lyric = Lyric.objects.get(id= lyric_id)
    serialized_data = LyricSerializer(lyric).data
    return Response(serialized_data)

@api_view(['DELETE',])
def delete_a_lyric(request,lyric_id):
    lyric = Lyric.objects.get(id= lyric_id)
    lyric.delete()
    return Response(status = status.HTTP_200_OK)

@api_view(['PUT',])
def update_a_lyric(request,lyric_id):
    lyric = Lyric.objects.get(id= lyric_id)
    serialized_data = LyricSerializer(lyric, data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data)