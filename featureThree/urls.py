from django.urls import path
from . import views

app_name='featureThree'
urlpatterns = [
    path('home', views.home, name='home'),
]