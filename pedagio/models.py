from django.db import models
from django.core.validators import RegexValidator

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=50)
    cpf = models.CharField(max_length=11)
    cnh = models.CharField(max_length=11, unique=True, default="12345678901")
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=15)


    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    motorista = models.ForeignKey(
        'Motorista', 
        on_delete=models.CASCADE, 
        related_name='veiculos'
    ) 
    placa = models.CharField(
        max_length=7, 
        unique=True,
        validators=[RegexValidator(
            r'^[A-Z]{3}\d{4}$|^[A-Z]{3}\d[A-Z]\d{2}$', 
            'Formato inválido. Use AAA-1234 ou ABC1D23.'
        )]
    )
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    categoria = models.CharField(
        max_length=20, 
        choices=[
            ('Carro', 'Carro'),
            ('Caminhão', 'Caminhão'),
            ('Ônibus', 'Ônibus')
        ]
    )

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

class Cadastro(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, unique=True, default='TAG_DEFAULT')

