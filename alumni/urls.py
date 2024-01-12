from rest_framework import routers

from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register('alumni', views.AlumniViewSet,basename='alumni')
router.register('article', views.ArticleViewSet,basename='article')

urlpatterns = [
    path('', include(router.urls))
]