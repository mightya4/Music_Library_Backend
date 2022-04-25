from lib2to3.refactor import MultiprocessRefactoringTool
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import MusicLibrarySerializer
from music_library.models import MusicLibrary

from music_library import serializer

# Create your views here.
@api_view(['GET', 'POST'])
def song_list(request):

    if request.method == 'GET':
        song = MusicLibrary.objects.all()
        serializer = MusicLibrarySerializer(song, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicLibrarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def song_detail(request, pk):
    songs = get_object_or_404(MusicLibrary, pk=pk)
    if request.method == 'GET':
        serializer = MusicLibrarySerializer(songs)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = MusicLibrarySerializer(songs, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)