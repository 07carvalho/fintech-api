from datetime import datetime
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from conta.models import Conta
from pessoa.models.pessoa import Pessoa


class TestDepositoApi(APITestCase):
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
        self.url = reverse('transacao_deposito', kwargs={'id_conta': self.conta.idConta})

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=self.cpf)

    def test_efetuar_deposito(self):
        data = {'valor': 100}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(100, float(Conta.objects.get(idPessoa=self.conta.idConta).saldo))

    def test_efetuar_deposito_valor_fracionado(self):
        data = {'valor': 10.01}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(10.01, float(Conta.objects.get(idPessoa=self.conta.idConta).saldo))

    def test_efetuar_deposito_sem_chave_valor(self):
        data = {'value': 100}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(400, response.status_code)

    def test_efetuar_deposito_com_valor_negativo(self):
        saldo_atual = self.conta.saldo
        data = {'valors': -100}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(400, response.status_code)
        self.assertEqual(saldo_atual, float(Conta.objects.get(idPessoa=self.conta.idConta).saldo))
