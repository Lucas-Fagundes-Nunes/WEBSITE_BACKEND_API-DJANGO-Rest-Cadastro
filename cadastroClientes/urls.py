from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from clientes.api import viewsets as clientesviewsets

route = routers.DefaultRouter()
route.register(r'clientes', clientesviewsets.ClientesViewSet, basename = 'Clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
