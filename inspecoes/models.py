from django.db import models


class Inspecao(models.Model):
    PLATAFORMAS = [('P-1', 'P-1'), ('P-2', 'P-2'), ('P-3', 'P-3'), ('P-4', 'P-4')]
    MODULOS = [(f'M{str(i).zfill(2)}', f'M{str(i).zfill(2)}') for i in range(1, 11)]
    SETORES = [('S01', 'S01'), ('S02', 'S02'), ('S03', 'S03')]
    TIPOS_EQUIPAMENTO = [
        ('Vaso de Pressão', 'Vaso de Pressão'),
        ('Tanque', 'Tanque'),
        ('Permutador', 'Permutador'),
        ('Filtro', 'Filtro')
    ]
    DEFEITOS = [
        ('Redução de espessura', 'Redução de espessura'),
        ('Vazamento', 'Vazamento'),
        ('Trinca', 'Trinca'),
        ('Desgaste anormal', 'Desgaste anormal'),
        ('Outro', 'Outro')
    ]
    CAUSAS = [
        ('Corrosão externa', 'Corrosão externa'),
        ('Corrosão interna', 'Corrosão interna'),
        ('Vibração excessiva', 'Vibração excessiva'),
        ('Impacto', 'Impacto'),
        ('Outro', 'Outro')
    ]
    CATEGORIAS_RTI = [('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')]
    RECOMENDACOES_RTI = [
        ('Reparar imediatamente', 'Reparar imediatamente'),
        ('Estender prazo de execução', 'Estender prazo de execução'),
        ('Interromper o serviço', 'Interromper o serviço'),
        ('Pintura', 'Pintura'),
        ('Outra', 'Outra')
    ]

    data_inspecao = models.DateField()
    tecnico_responsavel = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=3, choices=PLATAFORMAS)
    modulo = models.CharField(max_length=3, choices=MODULOS)
    setor = models.CharField(max_length=3, choices=SETORES)
    tipo_equipamento = models.CharField(max_length=20, choices=TIPOS_EQUIPAMENTO)
    tag = models.CharField(max_length=10)
    defeito = models.CharField(max_length=30, choices=DEFEITOS)
    causa = models.CharField(max_length=30, choices=CAUSAS)
    categoria_rti = models.CharField(max_length=3, choices=CATEGORIAS_RTI)
    recomendacao_rti = models.CharField(max_length=30, choices=RECOMENDACOES_RTI)
    observacoes = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return f'{self.tag} ({self.data_inspecao})'

