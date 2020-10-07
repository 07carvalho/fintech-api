from django.urls import path
from transacao.views.deposito import TransacaoDepositoApi
from transacao.views.saque import TransacaoSaqueApi


urlpatterns = [
    path('<int:id_conta>/transacoes/deposito', TransacaoDepositoApi.as_view(), name='transacao_deposito'),
    path('<int:id_conta>/transacoes/saque', TransacaoSaqueApi.as_view(), name='transacao_saque'),
]
