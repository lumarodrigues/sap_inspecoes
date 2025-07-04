from django.test import TestCase
from unittest.mock import patch
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class InspecaoMockedTest(APITestCase):

    @patch('inspecoes.views.requests.post')
    def test_criar_inspecao_com_envio_mockado(self, mock_post):
        mock_post.return_value.status_code = 200

        url = reverse('inspecao-list')
        data = {
            "data_inspecao": "2025-07-03",
            "tecnico_responsavel": "João Silva",
            "plataforma": "P-1",
            "modulo": "M01",
            "setor": "S01",
            "tipo_equipamento": "Vaso de Pressão",
            "tag": "VP-001",
            "defeito": "Redução de espessura",
            "causa": "Corrosão externa",
            "categoria_rti": "I",
            "recomendacao_rti": "Reparar imediatamente",
            "observacoes": "Inspeção realizada conforme padrão",
        }


        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        mock_post.assert_called_once()
        chamada_args, chamada_kwargs = mock_post.call_args

        self.assertIn('http://mock-sap.local/api/ordem-inspecao', chamada_args)

        enviado = chamada_kwargs.get('json', {})
        self.assertEqual(enviado['tecnico'], data['tecnico_responsavel'])
