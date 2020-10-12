from drf_yasg.utils import swagger_auto_schema
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from transacao.models.transacao import Transacao
from transacao.serializers.transacao import TransacaoSerializer


class TransacaoAPI(APIView):

    @swagger_auto_schema(responses={200: TransacaoSerializer()})
    def get(self, request, id_conta):
        ordem = request.query_params.get('ordem', '-dataTransacao')
        dias = int(request.query_params.get('dias', 7))
        if dias <= 90:
            transacoes = Transacao().listar_transacoes_por_conta(id_conta, ordem, dias)
            serializer = TransacaoSerializer(transacoes, many=True)
            return Response(serializer.data)
        msg = {'validation_error': 'A quantidade de dias deve ser menor ou igual a 90.'}
        raise exceptions.ValidationError(msg)
