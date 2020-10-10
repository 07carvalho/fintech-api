from rest_framework import serializers
from transacao.models.transacao import Transacao


class TransacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transacao
        # fields = '__all__'
        exclude = ('idConta', )