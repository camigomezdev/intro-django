from django.urls import path
from . import views

urlpatterns = [
    path('', views.ciudades, name='index'),
    path('ciudad/<int:id>', views.ciudad, name='ciudad'),
    path('ciudad/<int:id>/new_comment', views.new_comment, name='new_comment'),
]
