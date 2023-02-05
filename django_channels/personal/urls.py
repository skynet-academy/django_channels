from django.urls import path
from . import views
app_name = 'personal'

urlpatterns = [
        path('home', views.home, name='home'),
        ]
