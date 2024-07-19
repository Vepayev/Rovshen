from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert_list, name='insert_list'),
    path('add/', views.add_insert, name='add_insert'),
    path('edit/<int:pk>/', views.edit_insert, name='edit_insert'),
    path('delete/<int:pk>/', views.delete_insert, name='delete_insert'),
]
