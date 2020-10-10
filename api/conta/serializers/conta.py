from rest_framework import serializers
from conta.models.conta import Conta


class ContaSerializer(serializers.ModelSerializer):

    idPessoa = serializers.PrimaryKeyRelatedField(read_only=True)
    idConta = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Conta
        exclude = ('flagAtivo', )
