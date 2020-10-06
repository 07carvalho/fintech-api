from django.contrib import admin
from transacao.models.transacao import Transacao


@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    pass
