from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_redirect, name = 'dashboard_redirect'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('user/', views.user_dashboard, name='user_dashboard'),
]