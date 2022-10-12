from django.db import models
from artiste.models import Artiste
from datetime import datetime

# Create your models here.
class Song(models.Model):
    artist_id =  models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.IntegerField()

    def __str__(self) -> str:
        return self.title