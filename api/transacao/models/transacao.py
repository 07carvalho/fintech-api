from django.db import models
from conta.models.conta import Conta


class Transacao(models.Model):

    idTransacao = models.AutoField(primary_key=True)
    idConta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    dataTransacao = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        app_label = 'transacao'
        db_table = 'transacao'

    def __str__(self):
        return '{0} - {1} {2}'.format(self.idTransacao, self.valor, self.dataTransacao)

    @staticmethod
    def listar_transacoes_por_conta(id_conta: int, ordem: str = 'maisAntigas') -> 'Transacao':
        conta = Conta.obter_conta(id_conta)
        ordenacao = '-idTransacao' if ordem is 'maisAntigas' else 'idTransacao'
        return Transacao.objects.filter(idConta=conta).order_by(ordenacao)

    @staticmethod
    def efetua_deposito(id_conta: int, valor: float):
        conta = Conta.deposito(id_conta, valor)
        if conta is not None:
            transacao = Transacao.objects.create(
                idConta=conta, valor=valor
            )
            return transacao
        return None

    @staticmethod
    def efetua_saque(id_conta: int, valor: float):
        conta = Conta.saque(id_conta, valor)
        if conta is not None:
            transacao = Transacao.objects.create(
                idConta=conta, valor=valor
            )
            return transacao
        return None