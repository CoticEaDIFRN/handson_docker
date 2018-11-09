from rest_framework import serializers
from .models import Pedido


class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id', 'cliente_cpf', 'descricao')
