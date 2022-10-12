from django.urls import path
from .views import get_all_songs, get_a_song, delete_a_song, update_a_song, add_song

urlpatterns = [
    path('create-song/<int:artiste_id>', add_song, name='add_song'),
    path('delete-song/<int:song_id>', delete_a_song, name='delete_a_song'),
    path('get-song/<int:song_id>', get_a_song, name='get_a_song'),
    path('get-all-songs', get_all_songs, name='get_all_songs'),
    path('update-song/<int:song_id>', update_a_song, name='update_a_song'),
]