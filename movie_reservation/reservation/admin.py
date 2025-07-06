from django.contrib import admin
from .models import Genre, Movie, Showtime, Seat, Reservation
# Register your models here.

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Seat)
admin.site.register(Reservation)

