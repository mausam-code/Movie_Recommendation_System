from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Movie, Showtime, Reservation, Seat
from users.models import CustomUser


# Public home page (landing)
def home_page(request):
    movies = Movie.objects.all()
    return render(request, 'reservation/home.html', {'movies': movies})


# Check for admin
def is_admin(user):
    return user.is_authenticated and user.is_admin


# Redirect based on role
@login_required
def dashboard_redirect(request):
    if request.user.is_admin:
        return redirect('admin_dashboard')
    return redirect('user_dashboard')


# Admin Dashboard
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    context = {
        'movies': Movie.objects.all(),
        'showtimes': Showtime.objects.all(),
        'reservations': Reservation.objects.all(),
        'users': CustomUser.objects.filter(is_admin=False),
    }
    return render(request, 'reservation/admin_dashboard.html', context)


# User Dashboard
@login_required
def user_dashboard(request):
    now = timezone.now()
    reservations = Reservation.objects.filter(user=request.user, seat__showtime__start_time__gte=now)
    context = {
        'upcoming_reservations': reservations,
        'movies': Movie.objects.all()
    }
    return render(request, 'reservation/user_dashboard.html', context)
