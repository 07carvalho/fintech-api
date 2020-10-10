from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from transacao.models import Transacao
from transacao.serializers.transacao import TransacaoSerializer


class TransacaoDepositoApi(APIView):

    # @obter_pessoa
    @swagger_auto_schema(responses={200: TransacaoSerializer()})
    def post(self, request, id_conta):
        valor = request.data.get('valor', None)
        if valor is not None:
            transacao = Transacao.efetua_deposito(id_conta, valor)
            if transacao is not None:
                serializer = TransacaoSerializer(transacao)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
