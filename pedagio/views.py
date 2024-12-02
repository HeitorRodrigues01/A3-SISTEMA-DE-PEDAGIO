from django.http import JsonResponse
from pedagio.serializers import MotoristaSerializer, VeiculoSerializer, CadastroSerializer, ListaCadastrosMotoristaSerializer, ListaCadastrosVeiculoSerializer
from rest_framework import viewsets, generics
from pedagio.models import Motorista, Veiculo, Cadastro
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

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

    