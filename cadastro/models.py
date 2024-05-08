from django.db import models


class Ciclo(models.Model):
    campanha = models.CharField(max_length=7)


class Versao(models.Model):
    nomes_choices = (
        ('1', 'V1'),
        ('2', 'V2'),
        ('3', 'V3'),
        ('4', 'V4'),
        ('5', 'V5'),
        ('6', 'V6'),
    )
    nome = models.CharField(max_length=1, choices=nomes_choices)

    def __str__(self):
        return self.nome 

class Acabamento(models.Model):
    tipos_choices = (
        ('Q', 'Lombada quadrada'),
        ('C', 'Lombada canoa'),
        ('R', 'Refile'),
    )
    tipo = models.CharField(max_length=1, choices=tipos_choices, default='Q')
    
    def __str__(self):
        return self.tipo

class Papel(models.Model):
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)
    gramatura = models.IntegerField()
    bobina = models.IntegerField()
    cutoff = models.IntegerField()

    def __str__(self):
        return self.descricao 


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    tiragem = models.IntegerField()
    id_acabamento = models.ForeignKey(Acabamento, on_delete=models.DO_NOTHING)
    id_versao = models.ForeignKey(Versao, on_delete=models.DO_NOTHING)
    id_ciclo = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id_versao.nome 


class Caderno(models.Model):
    nome = models.CharField(max_length=10)
    paginacao = models.IntegerField()
    id_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    id_papel = models.ForeignKey(Papel, on_delete=models.DO_NOTHING)
    desp_acerto_interno = models.FloatField()
    desp_impressao_interno = models.FloatField()
    desp_acbto_interno = models.FloatField()
    desp_acerto_cliente = models.FloatField()
    desp_impressao_cliente = models.FloatField()
    desp_acbto_cliente = models.FloatField()
    papel_bruto_interno = models.FloatField()
    papel_bruto_cliente = models.FloatField()

    def __str__(self):
        return self.nome
