from rest_framework import viewsets

from desafio_fullstack.core.models import Estado, Cidade
from desafio_fullstack.core.serializers import EstadoSerializer, CidadeSerializer, CidadeDetailSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    serializer_class_detail = CidadeDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.serializer_class_detail
        else:
            return self.serializer_class
