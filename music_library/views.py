from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import MusicLibrarySerializer
from music_library.models import MusicLibrary

# Create your views here.
@api_view(['GET', 'POST'])
def music_list(request):

    if request.method == 'GET':
        music = MusicLibrary.objects.all()
        serializer = MusicLibrarySerializer(music, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicLibrarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def music_detail(request, pk):
    try:
        music = MusicLibrary.objects.get(pk=pk)
        serializer = MusicLibrarySerializer(music)
        return Response(serializer.data)

    except MusicLibrary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)