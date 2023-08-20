from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.movies),
    path('movie/<str:slug>', views.movie),
    path('customers/', views.customers),
    path('customer/<int:id>', views.customer),
]