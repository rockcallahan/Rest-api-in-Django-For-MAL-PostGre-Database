from django.urls import path
from .views import ListAnimeView,GetbyRank
from django.conf.urls import url
urlpatterns=[
    url(r'^$',ListAnimeView.as_view(),name='anime-all'),
    url(r'^rank/(?P<rank>[0-9]+)/$', GetbyRank.as_view(), name='GetByRank'),
]