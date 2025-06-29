from django.urls import path
from .views import home 
from legal_docs.views import LegalSearchView

urlpatterns = [
    path('', home, name='core-home'),
]
