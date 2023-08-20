from django.contrib import admin
from .models import Movie, Customer, CinemaSeance, Ticket

# Register your models here.
admin.site.register(Movie)
admin.site.register(Customer)
admin.site.register(CinemaSeance)
admin.site.register(Ticket)
