from rest_framework import serializers
import requests
from clientes import models

class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Clientes
        fields = '__all__'

    def validate_cpf(self, cpf):
        if len(str(cpf)) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 digitos")
        return cpf


    def validate_cep(self,  cep):
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
        if request:
            raise serializers.ValidationError("CEP inválido!")
        return cep

    
    def validate_telefone(self, telefone):
        if len(str(telefone)) < 8 or len(str(telefone)) > 13:
            raise serializers.ValidationError("Número de telefone inválido")
        return telefone
