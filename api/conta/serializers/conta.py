from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from conta.models.conta import Conta


class ContaSerializer(serializers.ModelSerializer):

    idPessoa = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Conta
        fields = '__all__'
