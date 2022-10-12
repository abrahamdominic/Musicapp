from django.shortcuts import render
from .models import Song
from artiste.models import Artiste
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer

@api_view(['POST',])
def add_song(request,artiste_id):
    artiste = Artiste.objects.get(id=artiste_id)
    song = Song(artist_id = artiste)
    serialized_data = SongSerializer(song,data = request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_all_songs(request):
    songs = Song.objects.all().order_by('-date_released')
    serialized_data = [SongSerializer(song).data for song in songs]
    return Response(serialized_data)

@api_view(['GET',])
def get_a_song(request,song_id):
    song = Song.objects.get(id= song_id)
    serialized_data = SongSerializer(song).data
    return Response(serialized_data)

@api_view(['DELETE',])
def delete_a_song(request,song_id):
    song = Song.objects.get(id= song_id)
    song.delete()
    return Response(status = status.HTTP_200_OK)

@api_view(['PUT',])
def update_a_song(request,song_id):
    song = Song.objects.get(id= song_id)
    serialized_data = SongSerializer(song, data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data)