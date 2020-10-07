from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from conta.models import Conta
from conta.serializers.conta import ContaSerializer
from conta.serializers.saldo import SaldoSerializer
from pessoa.decorators import obter_pessoa


class SaldoApi(APIView):
    serializer_class = ContaSerializer

    def get_object(self, id_conta):
        try:
            return Conta.objects.get(idConta=id_conta, flagAtivo=True)
        except Conta.DoesNotExist:
            raise exceptions.NotFound({'not_found': 'Esta conta não existe ou está desativada.'})

    # @obter_pessoa
    def get(self, request, id_conta):
        conta = self.get_object(id_conta)
        serializer = SaldoSerializer(conta)
        return Response(serializer.data, status=status.HTTP_200_OK)
