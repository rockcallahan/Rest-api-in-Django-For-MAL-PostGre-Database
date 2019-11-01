from django.urls import path
from .views import ListAnimeView
urlpatterns=[
    path('animes/',ListAnimeView.as_view(),name='anime-all')
]