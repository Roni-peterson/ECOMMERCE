from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import Produto, Endereco
from django.contrib.auth import logout, login

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

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('produtos')  # Substitua 'home' pelo nome da sua página inicial
    else:
        form = CustomAuthenticationForm()
    return render(request, 'produtos/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Substitua 'login' pelo nome da sua página de login

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('produtos')  # Substitua 'home' pelo nome da sua página inicial
    else:
        form = CustomUserCreationForm()
    return render(request, 'produtos/register.html', {'form': form})