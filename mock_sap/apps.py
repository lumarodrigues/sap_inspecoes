from django.apps import AppConfig


class MockSapConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mock_sap'
