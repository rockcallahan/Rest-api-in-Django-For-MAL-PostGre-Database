from django.urls import path
from .views import ListAnimeView,GetbyRank,GetTopten,GetSpringanime,Lastfive
from django.conf.urls import url
urlpatterns=[
    url(r'^$',ListAnimeView.as_view(),name='anime-all'),
    url(r'^rank/(?P<rank>[0-9]+)/$', GetbyRank.as_view(), name='GetByRank'),
    url(r'^pop10/$',GetTopten.as_view(),name='GetTopten'),
    url(r'^sprank/(?P<year>[0-9]+)/$',GetSpringanime.as_view(),name='GetSpringanime'),
    url(r'^last5/$',Lastfive.as_view(),name='Last5'),
    
]