from django.urls import path
from .views import ordem_inspecao


urlpatterns = [
    path('ordem-inspecao/', ordem_inspecao),
]
