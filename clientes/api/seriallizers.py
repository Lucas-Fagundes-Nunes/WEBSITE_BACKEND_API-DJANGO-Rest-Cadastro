import requests
from clientes import models
from rest_framework import serializers


class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Clientes
        fields = '__all__'

    def validate_cpf(self, cpf):
        for c in cpf:
            if (c == "0" or c == '1' or c == '2' or c == '3' or c== '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9'):
                print('É um número: ' + c)
            else:
                print('Não é número '+ c)
                raise serializers.ValidationError("O CPF deve conter apenas números ! Erro no caracter: "+c)
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
