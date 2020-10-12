from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from conta.models import Conta
from conta.serializers.conta import ContaSerializer
from conta.serializers.saldo import SaldoSerializer
from pessoa.decorators import obter_pessoa


class SaldoApi(APIView):
    serializer_class = ContaSerializer

    @swagger_auto_schema(responses={200: SaldoSerializer()})
    @obter_pessoa
    def get(self, request, pessoa):
        id_conta = self.kwargs.get('id_conta')
        conta = Conta.obter_conta(id_conta, pessoa)
        serializer = SaldoSerializer(conta)
        return Response(serializer.data, status=status.HTTP_200_OK)
