from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def search_legal_documents(request):
    return JsonResponse({'message': 'Legal search working!'})



class LegalSearchView(APIView):
    def post(self, request):
        query = request.data.get('query', '')
        if not query:
            return Response({"error": "Query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Temporary placeholder response
        return Response({"message": f"Searching for '{query}' in legal documents..."})
