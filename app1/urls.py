from django.urls import path
from . import views
from . views import logout_view

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('games',views.games,name='games'),
    path('location',views.location,name='location'),
    path('register',views.register,name='register'),
    path('loged',views.loged,name='loged'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('booking',views.booking,name='booking'),
    path('booked',views.booked,name='booked'),
    path('logout', logout_view, name='logout'),
]