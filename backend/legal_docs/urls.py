from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_legal_documents, name='search-legal-documents'),
]