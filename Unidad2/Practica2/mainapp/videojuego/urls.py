from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.videojuego_form, name='videojuego_insert'), 
    path('<int:id>', views.videojuego_form, name='videojuego_update'), 
    path('delete/<int:id>',views.videojuego_delete, name='videojuego_delete'),
    path('lista/', views.videojuego_list, name='videojuego_list')
]