from django.db import models
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
    dataCriacao = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        app_label = 'conta'
        db_table = 'contas'
        unique_together = [['idPessoa', 'tipoConta']]

    def __str__(self):
        return '{0} - {1} {2}'.format(self.idPessoa, self.idConta, self.tipoConta)