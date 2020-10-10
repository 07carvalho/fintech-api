from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from conta.models import Conta
from conta.serializers.conta import ContaSerializer
from pessoa.decorators import obter_pessoa


class ContaCreateApi(APIView):
    serializer_class = ContaSerializer

    @swagger_auto_schema(responses={200: ContaSerializer()})
    @obter_pessoa
    def post(self, request, pessoa):
        serializer = ContaSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(idPessoa=pessoa)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                raise exceptions.PermissionDenied({'error:': 'Usuário já possui uma conta deste tipo.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContaApi(APIView):
    serializer_class = ContaSerializer

    def delete(self, request, id_conta):
        conta = Conta.obter_conta(id_conta)
        conta.flagAtivo = False
        conta.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
