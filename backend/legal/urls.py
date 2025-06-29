from django.urls import path
from .views import LegalSearchView

urlpatterns = [
    path("search/", LegalSearchView.as_view(), name="legal-search"),
]
