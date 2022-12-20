from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('profile/',views.profileview,name='profile'),
    path('register/',views.registerview,name='register'),
    path('edit/',views.profileeditview,name='edit'),




]
