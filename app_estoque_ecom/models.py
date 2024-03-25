from django.db import models

class Produto(models.Model):
    cod_produto = models.IntegerField(primary_key=True)
    ean_produto = models.BigIntegerField(default=0)
    desc_produto = models.TextField(max_length=255)
    linha_produto = models.TextField(max_length=255)
    dt_val_produto = models.DateField()
    lt_produto = models.TextField(max_length=255)
    custo_produto = models.FloatField(default=0)

    def __str__(self):
        return self.desc_produto
    
class Endereco(models.Model):
    cod_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    rua = models.CharField(max_length=50)
    prateleira = models.CharField(max_length=50)
    caixa = models.CharField(max_length=50)
    estoque_produto = models.IntegerField()
    data_enderecamento = models.DateField()

    def __str__(self):
        return f"{self.cod_produto.desc_produto} - {self.rua} - {self.prateleira} - {self.caixa}"