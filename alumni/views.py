from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import Alumni, Article

from . import serializers, paginators


class AlumniViewSet(viewsets.ModelViewSet, generics.DestroyAPIView):
    queryset = Alumni.objects.all()
    serializer_class = serializers.AlumniSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = paginators.AlumniPaginator


class ArticleViewSet(viewsets.ModelViewSet, generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = paginators.AlumniPaginator