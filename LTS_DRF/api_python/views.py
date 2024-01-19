from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PythonSerializer
from .models import PythonModel


class PythonListAPIView(ListAPIView):
    queryset = PythonModel.objects.all()
    serializer_class = PythonSerializer


class PythonRetrieveAPIView(RetrieveAPIView):
    queryset = PythonModel.objects.all()
    serializer_class = PythonSerializer
