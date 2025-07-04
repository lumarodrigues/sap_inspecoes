from rest_framework import serializers
from .models import Inspecao


class InspecaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inspecao
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'inspecao-detail'}
        }

    def validate(self, data):
        tipo = data.get('tipo_equipamento')
        tag = data.get('tag')

        # Tipos de TAG válidas para cada equipamento
        tipos_validos = {
            'Vaso de Pressão': [f'VP-{i:03d}' for i in range(1, 51)],
            'Tanque': [f'TQ-{i:03d}' for i in range(1, 41)],
            'Permutador': [f'PM-{i:03d}' for i in range(1, 31)],
            'Filtro': [f'FT-{i:03d}' for i in range(1, 101)],
        }

        if tipo in tipos_validos:
            if tag not in tipos_validos[tipo]:
                raise serializers.ValidationError({
                    'tag': f'TAG inválida para {tipo}. Escolha alguma entre {tipos_validos[tipo][0]} até {tipos_validos[tipo][-1]}.'
                })

        return data
