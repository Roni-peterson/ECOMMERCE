from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app_estoque_ecom import views

urlpatterns = [
    #rota, view, nome referencia
    #pagina inicial
    path('', views.home, name='produtos'),
    #pagina cadastro de produtos
    path('cadastro-produtos/', views.cadastro_produtos, name='produtos'),

    path('enderecar/', views.enderecamento_produtos, name='enderecamento_produtos'),
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
