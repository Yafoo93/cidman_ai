from django.urls import path
from .views import home  # Make sure you have this view

urlpatterns = [
    path('', home, name='core-home'),
]
