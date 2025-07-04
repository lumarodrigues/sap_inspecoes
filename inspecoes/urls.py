from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InspecaoViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

router = DefaultRouter()
router.register(r'inspecao', InspecaoViewSet, basename='inspecao')

custom_urls = [
    path('inspecoes/', InspecaoViewSet.as_view({'get': 'list'}), name='inspecoes-list'),
]

urlpatterns = router.urls + custom_urls
