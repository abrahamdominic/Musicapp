from django.shortcuts import render
from .models import Artiste
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtisteSerializer

@api_view(['POST',])
def add_artiste(request):
    serialized_data = ArtisteSerializer(request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_all_artists(request):
    artists = Artiste.objects.all()
    serialized_data = [ArtisteSerializer(artiste).data for artiste in artists]
    return Response(serialized_data)

@api_view(['GET',])
def get_an_artiste(request,artiste_id):
    artiste = Artiste.objects.get(id= artiste_id)
    serialized_data = ArtisteSerializer(artiste).data
    return Response(serialized_data)

@api_view(['DELETE',])
def delete_an_artiste(request,artiste_id):
    artiste = Artiste.objects.get(id= artiste_id)
    artiste.delete()
    return Response(status = status.HTTP_200_OK)

@api_view(['PUT',])
def update_an_artiste(request,artiste_id):
    artiste = Artiste.objects.get(id= artiste_id)
    serialized_data = ArtisteSerializer(artiste, data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data)