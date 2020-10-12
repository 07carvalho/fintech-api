import pytz
from datetime import datetime, timedelta
from django.db import models
from conta.models.conta import Conta


class Transacao(models.Model):

    idTransacao = models.AutoField(primary_key=True)
    idConta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    dataTransacao = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        app_label = 'transacao'
        db_table = 'transacao'

    def __str__(self):
        return '{0} - {1} {2}'.format(self.idTransacao, self.valor, self.dataTransacao)

    @staticmethod
    def get_data(num_dias: int):
        return datetime.now(tz=pytz.UTC) - timedelta(days=num_dias)

    @staticmethod
    def get_data_meianoite(num_dias: int):
        return datetime.combine(datetime.now(tz=pytz.UTC), datetime.min.time()) - timedelta(days=num_dias)

    def listar_transacoes_por_conta(self, id_conta: int, ordem: str, dias: int) -> 'Transacao':
        conta = Conta.obter_conta(id_conta)
        return Transacao.objects.filter(
                    idConta=conta,
                    dataTransacao__gte=self.get_data_meianoite(dias)
                ).order_by(ordem)

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