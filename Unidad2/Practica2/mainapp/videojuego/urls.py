from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.videojuego_form, name='videjuego_insert'), 
    path('<int:id>', views.videojuego_form, name='videjuego_update'), 
    path('delete/<int:id>',views.videojuego_delete, name='videjuego_delete'),
    path('lista/', views.videojuego_list, name='videjuego_list')
]