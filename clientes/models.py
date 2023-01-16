from django.db import models

# Create your models here.
class Clientes(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome_completo = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    telefone = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    cep = models.IntegerField()
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=60)
    logradouro = models.CharField(max_length=20)
    criado = models.DateField(auto_now_add=True) 
