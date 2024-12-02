from rest_framework import serializers
from pedagio.models import Motorista, Veiculo, Cadastro

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = ['id', 'nome', 'email', 'cpf','cnh','data_nascimento','celular']

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'motorista', 'placa', 'modelo', 'ano', 'categoria']

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        exclude = []      

class ListaCadastrosMotoristaSerializer(serializers.ModelSerializer):
    modelo = serializers.ReadOnlyField(source='veiculo.modelo')  
    placa = serializers.ReadOnlyField(source='veiculo.placa')  
    tag = serializers.SerializerMethodField()
    class Meta:
        model = Cadastro
        fields = ['modelo', 'placa', 'tag']
    def get_tag(self, obj):
        return obj.tag

class ListaCadastrosVeiculoSerializer(serializers.ModelSerializer):
    motorista_nome = serializers.ReadOnlyField(source='motorista.nome')
    class Meta:
        model = Cadastro
        fields = ['motorista_nome']

