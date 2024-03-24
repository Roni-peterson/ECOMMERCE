from django.db import models

class Produto(models.Model):
    cod_produto = models.IntegerField(primary_key=True)
    ean_produto = models.BigIntegerField(default=0)
    desc_produto = models.TextField(max_length=255)
    linha_produto = models.TextField(max_length=255)
    dt_val_produto = models.DateField()
    lt_produto = models.TextField(max_length=255)