from rest_framework.viewsets import ModelViewSet
from .serializers import PedidoSerializer
from .models import Pedido


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
