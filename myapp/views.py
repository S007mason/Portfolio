from django.urls import path
from . import views

urlpatterns = [
    # Cambiamos 'lenguajes_view' por 'index' (o por el nombre correcto de tu función)
    path('', views.index, name='index'),
]

