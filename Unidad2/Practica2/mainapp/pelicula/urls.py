from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pelicula_form), 
    path('lista/', views.pelicula_list)
]