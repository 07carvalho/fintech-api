from drf_yasg.utils import swagger_auto_schema
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from conta.models import Conta
from pessoa.decorators import obter_pessoa
from transacao.models.transacao import Transacao
from transacao.serializers.transacao import TransacaoSerializer


class TransacaoAPI(APIView):

    @swagger_auto_schema(responses={200: TransacaoSerializer()})
    @obter_pessoa
    def get(self, request, pessoa):
        ordem = request.query_params.get('ordem', '-dataTransacao')
        dias = int(request.query_params.get('dias', 7))
        if dias <= 90:
            id_conta = self.kwargs.get('id_conta')
            conta = Conta.obter_conta(id_conta, pessoa)
            transacoes = Transacao().listar_transacoes_por_conta(conta, ordem, dias)
            serializer = TransacaoSerializer(transacoes, many=True)
            return Response(serializer.data)
        msg = {'validation_error': 'A quantidade de dias deve ser menor ou igual a 90.'}
        raise exceptions.ValidationError(msg)
