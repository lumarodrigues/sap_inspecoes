import requests
from rest_framework import viewsets
from .models import Inspecao
from .serializers import InspecaoSerializer


class InspecaoViewSet(viewsets.ModelViewSet):
    queryset = Inspecao.objects.all()
    serializer_class = InspecaoSerializer

    def perform_create(self, serializer):
        instancia = serializer.save()

        dados_para_sap = {
            'id': instancia.id,
            'data': instancia.data_inspecao.isoformat(),
            'tecnico': instancia.tecnico_responsavel,
        }

        # URL fictícia utilizada para simular o envio ao SAP PM pelo testcase
        url_sap = 'http://mock-sap.local/api/ordem-inspecao'

        try:
            response = requests.post(url_sap, json=dados_para_sap)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f'Erro ao enviar para SAP PM: {e}')
