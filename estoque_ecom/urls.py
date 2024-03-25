from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app_estoque_ecom import views

urlpatterns = [
    path('', views.home, name='produtos'),
    path('cadastro-produtos/', views.cadastro_produtos, name='cadastro_produtos'),
    path('cadastro-produtos/<int:produto_id>/', views.cadastro_produtos, name='cadastro_produtos'),
    path('enderecar/', views.enderecamento_produtos, name='enderecamento_produtos'),
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
