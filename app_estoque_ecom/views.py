from django.shortcuts import redirect, render
from .models import Produto

def home(request):
    return render(request,'produtos/home.html')

def cadastro_produtos(request):
    return render(request,'produtos/produtos.html')

#def produtos(request):
 #   if request.method == 'POST':
 #       print("Requisição POST recebida.")
  #      novo_produto = Produto()
   #     novo_produto.cod_produto = request.POST.get('cod_produto')
   #     novo_produto.ean_produto = request.POST.get('ean_produto')
  #      novo_produto.desc_produto = request.POST.get('desc_produto')
   #     novo_produto.linha_produto = request.POST.get('linha_produto')
   #     novo_produto.dt_val_produto = request.POST.get('dt_val_produto')
  #      novo_produto.lt_produto = request.POST.get('lt_produto')
   #     print("Dados do formulário recebidos:")
   #     print("Código do Produto:", request.POST.get('cod_produto'))
  #     print("EAN do Produto:", request.POST.get('ean_produto'))
  #      # Adicione mais linhas para outros campos, se necessário
   #     novo_produto.save()
  #      print("Produto salvo com sucesso!")
    

 #       produtos = {
 #           'produtos': Produto.objects.all()
 #       }

 #       return render(request,'produtos/home.html',produtos)
 #   else:
 #       print("Requisição não é POST.")

def produtos(request):
    if request.method == 'POST':
        # Cria um novo objeto Produto com dados fixos
        novo_produto = Produto(
            cod_produto=123,
            ean_produto='1234567890123',
            desc_produto='Produto de Teste',
            linha_produto='Linha de Teste',
            dt_val_produto='2024-12-31',
            lt_produto='Lote de Teste'
        )
        
        # Salva o objeto no banco de dados
        novo_produto.save()

        # Após salvar, redireciona para a página inicial ou outra página desejada
        return redirect('produtos')
    else:
        # Se não for uma requisição POST, renderiza a página normalmente
        return render(request, 'produtos/home.html')