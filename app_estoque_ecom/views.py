from django.shortcuts import get_object_or_404, render
from .models import Produto, Endereco

def home(request):
    produto = Produto.objects.all()
    return render(request,'produtos/home.html',{'produto':produto})

def cadastro_produtos(request, produto_id=None):
    if produto_id:
        produto = get_object_or_404(Produto, pk=produto_id)
        return render(request, 'produtos/produtos.html', {'produto': produto})
    else:
        # Se nenhum ID de produto for fornecido, listar todos os produtos
        produtos = Produto.objects.all()
        return render(request, 'produtos/produtos.html', {'produtos': produtos})


def enderecamento_produtos(request):
    endereco = Endereco.objects.all()
    return render(request,'produtos/enderecar.html',{'endereco':endereco})