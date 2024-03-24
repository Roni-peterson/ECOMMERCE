from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request,'produtos/home.html')

def cadastro_produtos(request):
    return render(request,'produtos/produtos.html')

def enderecamento_produtos(request):
    return render(request,'produtos/enderecar.html')

def produtos(request):
    if request.method == 'POST':
        print("Requisição POST recebida.")
        novo_produto = Produto()
        novo_produto.cod_produto = request.POST.get('cod_produto')
        novo_produto.ean_produto = request.POST.get('ean_produto')
        novo_produto.desc_produto = request.POST.get('desc_produto')
        novo_produto.linha_produto = request.POST.get('linha_produto')
        novo_produto.dt_val_produto = request.POST.get('dt_val_produto')
        novo_produto.lt_produto = request.POST.get('lt_produto')
        print("Dados do formulário recebidos:")
        print("Código do Produto:", request.POST.get('cod_produto'))
        print("EAN do Produto:", request.POST.get('ean_produto'))
        # Adicione mais linhas para outros campos, se necessário
        novo_produto.save()
        print("Produto salvo com sucesso!")
    

        produtos = {
            'produtos': Produto.objects.all()
        }

        return render(request,'produtos/home.html',produtos)
    else:
        print("Requisição não é POST.")
