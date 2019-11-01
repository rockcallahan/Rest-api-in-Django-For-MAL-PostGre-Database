from rest_framework import generics
from.serializers import  AnimeSerializer
from .models import anime
class ListAnimeView(generics.ListAPIView):
    queryset= anime.objects.all()
    serializer_class=AnimeSerializer
# Create your views here.
