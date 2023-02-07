from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import booking, menu
from .serializers import bookingSerializer, menuSerializer

class menuview(APIView):
    def get(self, request):
        items = menu.objects.all()
        serializer = menuSerializer(items, many=True)
        return Response(serializer.data) # return JSON
    def post(self, request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", 
                            "data": serializer.data}) # return JSON

class bookingview(APIView):
    def get(self, request):
        items = booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data) # return JSON
    def post(self, request):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", 
                            "data": serializer.data}) # return JSON

def index(request):
    return render(request, 'index.html', {})