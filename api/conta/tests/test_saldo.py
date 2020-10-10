from datetime import datetime
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from conta.models import Conta
from pessoa.models.pessoa import Pessoa


class TestSaqueApi(APITestCase):
    cpf = '12345678901'

    def setUp(self) -> None:
        data = {
            'nome': 'Fulano de Tal',
            'cpf': self.cpf,
            'dataNascimento': datetime.strptime('1980/01/30', '%Y/%m/%d')
        }
        self.pessoa = Pessoa.objects.create(**data)

        conta = {
            'idPessoa': self.pessoa,
            'limiteSaqueDiario': 1000,
            'tipoConta': 1
        }
        self.conta = Conta.objects.create(**conta)
        self.conta.saldo = 100
        self.conta.save()
        self.url = reverse('consulta_saldo', kwargs={'id_conta': self.conta.idConta})

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=self.cpf)

    def test_consulta_saldo(self):
        response = self.client.get(self.url)
        saldo_atual = '{:.2f}'.format(self.conta.saldo)
        self.assertEqual(200, response.status_code)
        self.assertEqual(saldo_atual, response.data.get('saldo'))

    def test_consulta_saldo_conta_inativa(self):
        self.conta.flagAtivo = False
        self.conta.save()
        response = self.client.get(self.url)
        self.assertEqual(404, response.status_code)