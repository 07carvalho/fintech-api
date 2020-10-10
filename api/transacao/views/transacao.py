from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from transacao.models.transacao import Transacao
from transacao.serializers.transacao import TransacaoSerializer


class TransacaoAPI(APIView):

    @swagger_auto_schema(responses={200: TransacaoSerializer()})
    def get(self, request, id_conta):
        transacoes = Transacao.listar_transacoes_por_conta(id_conta)
        serializer = TransacaoSerializer(transacoes, many=True)
        return Response(serializer.data)
