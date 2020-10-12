from datetime import datetime
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from conta.enums import Conta
from pessoa.models.pessoa import Pessoa


class TestContasApi(APITestCase):
    cpf = '12345678901'
    url = reverse('criar_conta')

    def setUp(self) -> None:
        data = {
            'nome': 'Fulano de Tal',
            'cpf': self.cpf,
            'dataNascimento': datetime.strptime('1980/01/30', '%Y/%m/%d')
        }
        self.pessoa = Pessoa.objects.create(**data)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=self.cpf)

    def test_criar_conta_corrente_nova(self):
        data = {'limiteSaqueDiario': 100, 'tipoConta': Conta.CONTA_POUPANCA.value}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(201, response.status_code)

    def test_criar_duas_contas_mesmo_tipo(self):
        # primeia request retorna 200 e a segunda 403 (forbidden)
        status = [201, 403]
        for s in status:
            data = {'limiteSaqueDiario': 100, 'tipoConta': Conta.CONTA_POUPANCA.value}
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(s, response.status_code)

    def test_criar_conta_tipo_invalido(self):
        data = {'limiteSaqueDiario': 100, 'tipoConta': 4}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(400, response.status_code)
