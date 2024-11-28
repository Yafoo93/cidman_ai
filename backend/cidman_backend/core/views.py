from django.shortcuts import render
from rest_framework import viewsets
from .models import Case
from .serializers import CaseSerializer


# Create your views here.
class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

