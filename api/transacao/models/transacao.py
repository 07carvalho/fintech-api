from django.db import models
from conta.models.conta import Conta


class Transacao(models.Model):

    idTransacao = models.AutoField(primary_key=True)
    idConta = models.ForeignKey(Conta, on_delete=models.CASCADE())
    valor = models.DecimalField(decimal_places=2)
    dataTransacao = models.DateField(auto_now_add=True, editable=False)
