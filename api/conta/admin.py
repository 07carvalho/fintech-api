from django.contrib import admin
from conta.models.conta import Conta


@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    pass
