from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from pedagio.serializers import MotoristaSerializer, VeiculoSerializer, CadastroSerializer, ListaCadastrosMotoristaSerializer, ListaCadastrosVeiculoSerializer
from rest_framework import viewsets, generics
from pedagio.models import Motorista, Veiculo, Cadastro
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


def index(request):
    return render(request, 'index.html')

def fale_conosco(request):
    return render(request, 'fale_conosco.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def membros(request):
    return render(request, 'membros.html')

def area_restrita(request):
    return render(request, 'arearestrita.html')

@login_required 
def dashboard(request):
    return render(request, 'dashboard.html')

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
    
class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer   

class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer      

class ListaCadastroMotorista(generics.ListAPIView):
    def get_queryset(self):
        queryset = Cadastro.objects.filter(motorista_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCadastrosMotoristaSerializer

class ListaCadastroVeiculo(generics.ListAPIView):
    def get_queryset(self):
        queryset = Cadastro.objects.filter(veiculo_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCadastrosVeiculoSerializer 

    