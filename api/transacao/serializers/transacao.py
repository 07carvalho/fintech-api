from datetime import datetime
from rest_framework import serializers
from transacao.models.transacao import Transacao


class TransacaoSerializer(serializers.ModelSerializer):

    dataTransacao = serializers.SerializerMethodField()

    def get_dataTransacao(self, obj):
        return datetime.strftime(obj.dataTransacao, '%d/%m/%Y %H:%M:%S')

    class Meta:
        model = Transacao
        exclude = ('idConta', )
