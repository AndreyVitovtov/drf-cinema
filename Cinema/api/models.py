from django.db import models
from django.utils.text import slugify


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    rating = models.FloatField()
    description = models.TextField(max_length=2000)
    slug = models.CharField(max_length=250, default="", editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()


class CinemaSeance(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    places = models.IntegerField()

    def __str__(self):
        return f"{self.movie.title} {self.datetime}"


class Ticket(models.Model):
    seance = models.ForeignKey(CinemaSeance, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.seance.movie.title} {self.price}"


class Customer(models.Model):
    user_name = models.CharField(max_length=100)
    tickets = models.ManyToManyField(Ticket)

    def __str__(self):
        return f"{self.user_name}"
