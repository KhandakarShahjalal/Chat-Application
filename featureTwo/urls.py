from django.urls import path
from . import views

app_name='featureTwo'
urlpatterns = [
    path('home', views.home, name='home'),
]