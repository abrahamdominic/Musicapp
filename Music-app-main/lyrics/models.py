from email.policy import default
from django.db import models
from song.models import Song
from datetime import datetime

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content= models.TextField(default= " ")
    
    def __str__(self) -> str:
        return self.song_id.title 