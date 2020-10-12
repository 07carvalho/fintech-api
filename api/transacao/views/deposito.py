from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pessoa.decorators import obter_pessoa
from conta.models import Conta
from transacao.models import Transacao
from transacao.serializers.transacao import TransacaoSerializer


class TransacaoDepositoApi(APIView):

    @swagger_auto_schema(responses={200: TransacaoSerializer()})
    @obter_pessoa
    def post(self, request, pessoa):
        valor = request.data.get('valor', None)
        if valor is not None:
            id_conta = self.kwargs.get('id_conta')
            conta = Conta.obter_conta(id_conta, pessoa)
            transacao = Transacao.efetua_deposito(conta.idConta, valor)
            if transacao is not None:
                serializer = TransacaoSerializer(transacao)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
