from django.urls import path
from conta.views.conta import ContaCreateApi, ContaApi
from conta.views.saldo import SaldoApi

urlpatterns = [
    path('contas', ContaCreateApi.as_view(), name='criar_conta'),
    path('contas/<int:id_conta>', ContaApi.as_view(), name='conta_api'),
    path('contas/<int:id_conta>/saldo', SaldoApi.as_view(), name='consulta_saldo'),
]
