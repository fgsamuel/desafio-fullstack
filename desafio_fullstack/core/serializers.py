from rest_framework import serializers

from desafio_fullstack.core.models import Estado, Cidade


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'


class CidadeDetailSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(many=False)

    class Meta:
        model = Cidade
        fields = '__all__'
