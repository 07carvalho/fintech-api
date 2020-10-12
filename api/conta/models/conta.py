from decimal import Decimal
from django.db import models, transaction
from rest_framework import exceptions

from pessoa.models.pessoa import Pessoa


class Conta(models.Model):

    TYPE = (
        (1, 'Conta Corrente - Pessoa Física'),
        (2, 'Conta Poupança'),
        (3, 'Conta Corrente - Pessoa Jurídica'),
    )

    idConta = models.AutoField(primary_key=True)
    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=9, default=0, decimal_places=2, blank=False, null=False)
    limiteSaqueDiario = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    flagAtivo = models.BooleanField(default=True, blank=False, null=False)
    tipoConta = models.IntegerField(choices=TYPE)
    dataCriacao = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        app_label = 'conta'
        db_table = 'contas'
        unique_together = [['idPessoa', 'tipoConta']]

    def __str__(self):
        return '{0} - {1} {2}'.format(self.idPessoa, self.idConta, self.tipoConta)

    @staticmethod
    def obter_conta(id_conta: int, pessoa: 'Pessoa') -> 'Conta':
        try:
            return Conta.objects.get(idConta=id_conta, idPessoa=pessoa, flagAtivo=True)
        except Conta.DoesNotExist:
            raise exceptions.NotFound({'not_found': 'Esta conta não existe ou está desativada.'})

    @classmethod
    def deposito(cls, id_conta: int, valor: float) -> 'Conta':
        with transaction.atomic():
            conta = (
                cls.objects.select_for_update().get(idConta=id_conta)
            )
            if conta.flagAtivo and valor >= 0:
                conta.saldo += Decimal(valor)
                conta.save()
                return conta
        return None

    @classmethod
    def saque(cls, id_conta: int, valor: float) -> 'Conta':
        with transaction.atomic():
            conta = (
                cls.objects.select_for_update().get(idConta=id_conta)
            )
            if conta.flagAtivo and valor >= 0:
                if conta.saldo < valor:
                    raise exceptions.PermissionDenied(
                        detail={'saldo_error': 'Saldo insuficiente para efetuar o saque'})
                conta.saldo -= valor
                conta.save()
                return conta
        return None
