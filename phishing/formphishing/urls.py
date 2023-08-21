from django.urls import path
from . import views

urlpatterns = [
    path('', views.guardar_usuario, name='guardar_usuario'),
    path('mostrar_usuarios/', views.mostrar_usuarios, name='mostrar_usuarios'),
]