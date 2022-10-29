from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.serie_form, name='serie_insert'), 
    path('<int:id>', views.serie_form, name='serie_update'), 
    path('delete/<int:id>',views.serie_delete, name='serie_delete'),
    path('lista/', views.serie_list, name='serie_list')
]