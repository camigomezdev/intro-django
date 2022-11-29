from django.urls import path
from . import views

urlpatterns = [
    path('ciudad/<int:id>', views.ciudad, name='ciudad'),
    path('', views.ciudades, name='index'),
]
