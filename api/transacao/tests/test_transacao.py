import pytz
from datetime import datetime
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from conta.models import Conta
from pessoa.models.pessoa import Pessoa
from transacao.models.transacao import Transacao


class TestTransacaoApi(APITestCase):
    cpf = '12345678901'

    def setUp(self) -> None:
        data = {
            'nome': 'Fulano de Tal',
            'cpf': self.cpf,
            'dataNascimento': datetime(1980, 1, 30, 1, 1, 1, tzinfo=pytz.UTC)
        }
        self.pessoa = Pessoa.objects.create(**data)

        conta = {
            'idPessoa': self.pessoa,
            'limiteSaqueDiario': 1000,
            'tipoConta': 1
        }
        self.conta = Conta.objects.create(**conta)

        dias = [1, 7, 30, 60, 90, 120]
        for d in dias:
            transacao= {'idConta': self.conta, 'valor': 100}
            obj = Transacao.objects.create(**transacao)
            obj.dataTransacao = Transacao.get_data(d)
            obj.save()

        self.url = reverse('transacao_conta', kwargs={'id_conta': self.conta.idConta})

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=self.cpf)

    def test_lista_transacao_sem_campos(self):
        """data default eh de 7 dias e ordem eh da mais antiga para a mais nova"""
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.data))
        self.assertEqual(True, datetime.strptime(response.data[0].get('dataTransacao'), '%d/%m/%Y %H:%M:%S') >
                                datetime.strptime(response.data[1].get('dataTransacao'), '%d/%m/%Y %H:%M:%S'))

    def test_lista_transacao_30_dias(self):
        params = {'dias': 30}
        response = self.client.get(self.url, params)
        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(response.data))

    def test_lista_transacao_90_dias(self):
        params = {'dias': 90}
        response = self.client.get(self.url, params)
        self.assertEqual(200, response.status_code)
        self.assertEqual(5, len(response.data))

    def test_lista_transacao_ordem_mais_nova(self):
        params = {'ordem': 'dataTransacao'}
        response = self.client.get(self.url, params)
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, datetime.strptime(response.data[1].get('dataTransacao'), '%d/%m/%Y %H:%M:%S') >
                                datetime.strptime(response.data[0].get('dataTransacao'), '%d/%m/%Y %H:%M:%S'))
