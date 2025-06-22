from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Case
# from .serializers import CaseSerializer
from django.http import JsonResponse


# Create your views here.
# class CaseViewSet(viewsets.ModelViewSet):
 #   queryset = Case.objects.all()
  #  serializer_class = CaseSerializer

def home(request):
    return JsonResponse({"message": "CIDMAN-AI Core API is running ✅"})

