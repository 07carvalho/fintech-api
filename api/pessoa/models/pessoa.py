from django.db import models


class Pessoa(models.Model):
    idPessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    dataNascimento = models.DateTimeField(blank=False, null=False)

    class Meta:
        app_label = 'pessoa'
        db_table = 'pessoas'

    def __str__(self):
        return '{0} - {1} {2}'.format(self.idPessoa, self.nome, self.cpf)
