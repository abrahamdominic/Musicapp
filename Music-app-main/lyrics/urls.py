from django.urls import path
from .views import get_all_lyrics, get_a_lyric, delete_a_lyric, update_a_lyric, add_lyric

urlpatterns = [
    path('create-lyric/<int:song_id>', add_lyric, name='add_lyric'),
    path('delete-lyric/<int:lyric_id>', delete_a_lyric, name='delete_a_lyric'),
    path('get-lyric/<int:lyric_id>', get_a_lyric, name='get_a_lyric'),
    path('get-all-lyrics', get_all_lyrics, name='get_all_lyrics'),
    path('update-lyric/<int:lyric_id>', update_a_lyric, name='update_a_lyric'), 
]