from django.urls import path
from .views import get_all_artists, get_an_artiste, delete_an_artiste, update_an_artiste, add_artiste

urlpatterns = [
    path('create-artiste', add_artiste, name='add_artiste'),
    path('delete-artiste/<artiste_id>', delete_an_artiste, name='delete_an_artiste'),
    path('get-artiste/<artiste_id>', get_an_artiste, name='get_an_artiste'),
    path('get-all-artists', get_all_artists, name='get_all_artists'),
    path('update-artiste/<artiste_id>', update_an_artiste, name='update_an_artiste'),
]