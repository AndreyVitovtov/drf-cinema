from rest_framework import serializers

from . import models


class SerializedMovie(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['title', 'rating', 'description', 'slug']


class SerializedCinemaSeance(serializers.ModelSerializer):
    class Meta:
        model = models.CinemaSeance
        fields = ['movie', 'datetime', 'places']


class SerializedTicket(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ['seance', 'price']


class SerializedCustomer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id', 'user_name', 'tickets']
