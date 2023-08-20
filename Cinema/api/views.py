from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


# Create your views here.

@api_view(['GET'])
def movies(request):
    movies = models.Movie.objects.all()
    serialized_movies = serializers.SerializedMovie(movies, many=True)
    return Response(serialized_movies.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie(request, slug):
    movie = models.Movie.objects.get(slug=slug)
    serialized_movie = serializers.SerializedMovie(movie)
    return Response(serialized_movie.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def customers(request):
    customers = models.Customer.objects.all()
    serialized_customers = serializers.SerializedCustomer(customers, many=True)
    return Response(serialized_customers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def customer(request, id):
    customer = models.Customer.objects.get(id=id)
    serialized_customer = serializers.SerializedCustomer(customer)
    return Response(serialized_customer.data, status=status.HTTP_200_OK)
