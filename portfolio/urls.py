# portfolio/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views  # Asegúrate de que 'myapp' sea el nombre correcto de tu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
