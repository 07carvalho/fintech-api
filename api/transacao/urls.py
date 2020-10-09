from django.urls import path
from transacao.views.deposito import TransacaoDepositoApi
from transacao.views.saque import TransacaoSaqueApi
from transacao.views.transacao import TransacaoAPI


urlpatterns = [
    path('contas/<int:id_conta>/transacoes', TransacaoAPI.as_view(), name='transacao_conta'),
    path('contas/<int:id_conta>/transacoes/deposito', TransacaoDepositoApi.as_view(), name='transacao_deposito'),
    path('contas/<int:id_conta>/transacoes/saque', TransacaoSaqueApi.as_view(), name='transacao_saque'),
]
