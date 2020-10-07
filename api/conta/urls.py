from django.urls import path
from conta.views.conta import ContaCreateApi

urlpatterns = [
    path('', ContaCreateApi.as_view(), name='criar_conta'),
]
