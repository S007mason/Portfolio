from django.urls import path
from . import views  # Esto importa las vistas desde el archivo views.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.lenguajes_view, name='index'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)