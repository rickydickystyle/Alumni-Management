from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import Alumni

from . import serializers



class AlumniViewSet(viewsets.ModelViewSet, generics.DestroyAPIView):
    queryset = Alumni.objects.all()
    serializer_class = serializers.AlumniSerializer
    permission_classes = [permissions.AllowAny]