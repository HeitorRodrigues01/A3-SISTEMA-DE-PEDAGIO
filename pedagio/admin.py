from django.contrib import admin
from pedagio.models import Motorista, Veiculo, Cadastro

class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'cnh', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(Motorista, MotoristaAdmin)

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'motorista', 'placa', 'modelo', 'ano', 'categoria')
    list_display_links = ('id', 'placa')
    search_fields = ('placa',)  

admin.site.register(Veiculo, VeiculoAdmin)

class CadastroAdmin(admin.ModelAdmin):
    list_display = ('id', 'motorista','veiculo','tag')
    list_display_links = ('id',)

admin.site.register(Cadastro, CadastroAdmin)

