from django.urls import path, include
from . import views

urlpatterns = [
    path('insert', views.pelicula_form, name='pelicula_insert'), 
    path('<int:id>', views.pelicula_form, name='pelicula_update'), 
    path('delete/<int:id>',views.pelicula_delete, name='pelicula_delete'),
    path('lista/', views.pelicula_list, name='pelicula_list'),
    path('', views.homepage, name='homepage')
]