from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from clientes.api import seriallizers
from clientes import models

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = models.Clientes.objects.all()
    serializer_class = seriallizers.ClientesSerializers
    

    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'cpf', 'nome_completo']




