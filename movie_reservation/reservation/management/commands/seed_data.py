from django.core.management.base import BaseCommand
from reservation.models import Genre,Movie,Showtime,Seat
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = "Seed database with test data"

    def handle(self, *args, **kwargs):
        #genres
        action = Genre.objects.get_or_create(name="Action")[0]
        drama = Genre.objects.get_or_create(name="Drama")[0]

        movie1 = Movie.objects.get_or_create(
            title="Avengers",
            description = "Superhero Action",
            genre = action
        )[0]

        movie2 = Movie.objects.get_or_create(
            title = "Inception",
            description = "Dream within a dream",
            genre = drama
        )[0]

        # Showtimes (next 3 days)
        for i in range(3):
            for movie in [movie1,movie2]:
                start = timezone.now() + timedelta(days=i, hours =18)
                showtime, _ = Showtime.objects.get_or_create(
                    movie = movie,
                    start_time = start,
                    defaults = {'capacity':30}
                )

                # create 30 seats(A1-A30)

                for n in  range(1,31):
                    Seat.objects.get_or_create(
                        showtime=showtime,
                        seat_number = f"A{n}"
                    )

        self.stdout.write(self.style.SUCCESS("Seeded genres, movies, showtimes and seats"))