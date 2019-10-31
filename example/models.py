from django.db import models


class anime(models.Model):
    title = models.TextField()
    rank=models.PositiveSmallIntegerField()
    score=models.FloatField()
    users_rated=models.PositiveIntegerField()
    Popularity=models.PositiveSmallIntegerField()
    Favorites=models.PositiveIntegerField()
    Members=models.PositiveIntegerField()
    animeType=models.CharField(max_length=100)
    Episodes=models.PositiveSmallIntegerField()
    status=models.CharField(max_length=100)
    premiered=models.CharField(max_length=100)
    studio=models.CharField(max_length=100)
    source=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    genres=models.TextField()
    def __str__(self):
        return self.title
