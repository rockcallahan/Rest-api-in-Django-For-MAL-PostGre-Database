from rest_framework import generics
from.serializers import  AnimeSerializer
from .models import anime
from django.http import HttpResponse

class ListAnimeView(generics.ListAPIView):
    queryset= anime.objects.all()
    serializer_class=AnimeSerializer

class GetbyRank(generics.ListAPIView):
    serializer_class=AnimeSerializer
    def get_queryset(self):
        rank=self.kwargs['rank']
        return anime.objects.filter(rank=rank)
