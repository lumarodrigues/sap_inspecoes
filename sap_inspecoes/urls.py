from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Inspeções Técnicas API",
        default_version='v1',
        description="Documentação da API para inspeções e integração com SAP PM",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('inspecoes.urls')),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include('mock_sap.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
