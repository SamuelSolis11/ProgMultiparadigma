from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.documental_form, name='documental_insert'), 
    path('<int:id>', views.documental_form, name='documental_update'), 
    path('delete/<int:id>',views.documental_delete, name='documental_delete'),
    path('lista/', views.documental_list, name='documental_list')
]