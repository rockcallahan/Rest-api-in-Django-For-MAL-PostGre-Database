from rest_framework import generics
from.serializers import  AnimeSerializer
from .models import anime
from django.http import HttpResponse
from datetime import datetime

class ListAnimeView(generics.ListAPIView):
    queryset= anime.objects.all()
    serializer_class=AnimeSerializer

class GetbyRank(generics.ListAPIView):
    serializer_class=AnimeSerializer
    def get_queryset(self):
        rank=self.kwargs['rank']
        return anime.objects.filter(rank=rank)


class GetTopten(generics.ListAPIView):
    serializer_class=AnimeSerializer
    def get_queryset(self):
        sorted=anime.objects.order_by('Popularity')
        return sorted[:10]

class GetSpringanime(generics.ListAPIView):
    serializer_class=AnimeSerializer
    def get_queryset(self):
        year=int(self.kwargs['year'])
        i=0
        spring3=anime.objects.filter(premiered='Spring'+' '+str(year))
        while i<5:
            year=year-1
            spring2=anime.objects.filter(premiered='Spring'+' '+str(year))
            spring3=spring3.union(spring2)
            i=i+1
        final=spring3.order_by('rank')
        return final


class Lastfive(generics.ListAPIView):
    serializer_class=AnimeSerializer
    def get_queryset(self):
        year=int(datetime.now().year)
        i=0
        spring3=anime.objects.filter(premiered='Spring'+' '+str(year))
        while i<5:
            year=year-1
            spring2=anime.objects.filter(premiered='Spring'+' '+str(year))
            spring3=spring3.union(spring2)
            i=i+1
        final=spring3.order_by('rank')
        return final







        


