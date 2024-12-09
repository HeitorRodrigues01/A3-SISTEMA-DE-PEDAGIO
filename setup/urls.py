"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pedagio import views 
from pedagio.views import MotoristaViewSet, VeiculoViewSet, CadastroViewSet, ListaCadastroMotorista, ListaCadastroVeiculo
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(prefix='motoristas', viewset=MotoristaViewSet, basename='motoristas')
router.register(prefix='veiculos', viewset=VeiculoViewSet, basename='veiculos')
router.register(prefix='cadastros', viewset=CadastroViewSet, basename='Cadastros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('fale-conosco/', views.fale_conosco, name='fale_conosco'),
    path('membros/', views.membros, name='membros'),
    path('area-restrita/', views.area_restrita, name='area_restrita'),
    path('sobre/', views.sobre, name='sobre'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('servicos/', views.servicos, name='servicos'),
    path('', include(router.urls)),
    path('motoristas/<int:pk>/cadastros/', ListaCadastroMotorista.as_view()),
    path('veiculos/<int:pk>/cadastros/', ListaCadastroVeiculo.as_view()),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
