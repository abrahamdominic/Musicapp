from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/song/',include('song.urls')),
    path('api/lyrics/',include('lyrics.urls')),
    path('api/artiste/', include('artiste.urls'))
]
