from django.urls import path
from .views import ListAnimeView,GetbyRank,GetTopten
from django.conf.urls import url
urlpatterns=[
    url(r'^$',ListAnimeView.as_view(),name='anime-all'),
    url(r'^rank/(?P<rank>[0-9]+)/$', GetbyRank.as_view(), name='GetByRank'),
    url(r'^pop10/$',GetTopten.as_view(),name='GetTopten')
    
]