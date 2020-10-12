from datetime import datetime
from rest_framework import serializers
from conta.models.conta import Conta


class ContaSerializer(serializers.ModelSerializer):

    idPessoa = serializers.PrimaryKeyRelatedField(read_only=True)
    idConta = serializers.PrimaryKeyRelatedField(read_only=True)
    dataCriacao = serializers.SerializerMethodField()

    def get_dataCriacao(self, obj):
        return datetime.strftime(obj.dataCriacao, '%d/%m/%Y %H:%M:%S')

    class Meta:
        model = Conta
        exclude = ('flagAtivo', )
