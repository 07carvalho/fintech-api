from django.contrib import admin
from pessoa.models.pessoa import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass
