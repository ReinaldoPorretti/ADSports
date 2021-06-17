from django.db import models

# Create your models here.


class Pedido(models.Model):
    data_compra = models.DateField(max_length=8)
    cliente = models.CharField(max_length=150)
    produtos = models.CharField(max_length=150)
    valor = models.FloatField()

class Produtos(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    preco = models.FloatField()
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=150)

class Carrinho(models.Model):
    nome_usuario = models.CharField(max_length=150)
    nome_produto = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits= 8, decimal_places=2)
    quantidade = models.IntegerField()
    total = models.DecimalField(max_digits= 8, decimal_places=2)
    
        

