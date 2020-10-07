from rest_framework import serializers
from conta.models.conta import Conta


class SaldoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conta
        fields = ['saldo',]
