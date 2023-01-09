from django.urls import path
from . import views

app_name='featureOne'
urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.aboutus, name='aboutus'),
]