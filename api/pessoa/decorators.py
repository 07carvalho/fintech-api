from rest_framework.exceptions import PermissionDenied, NotFound
from pessoa.models.pessoa import Pessoa


def obter_pessoa(operation):
    def wrapper(api, request, **kwargs):
        cpf = request.META.get('HTTP_AUTHORIZATION', None)
        if cpf is not None:
            try:
                pessoa = Pessoa.objects.get(cpf=cpf)
                return operation(api, request, pessoa)
            except Pessoa.DoesNotExist:
                raise NotFound
        raise PermissionDenied
    return wrapper
