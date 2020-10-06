# Generated by Django 2.2.12 on 2020-10-06 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('idConta', models.AutoField(primary_key=True, serialize=False)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('limiteSaqueDiario', models.DecimalField(decimal_places=2, max_digits=9)),
                ('flagAtivo', models.BooleanField(default=True)),
                ('tipoConta', models.IntegerField(choices=[(1, 'Conta Corrente - Pessoa Física'), (2, 'Conta Poupança'), (3, 'Conta Corrente - Pessoa Jurídica')])),
                ('dataCriacao', models.DateField(auto_now_add=True)),
                ('idPessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
            options={
                'db_table': 'contas',
                'unique_together': {('idPessoa', 'tipoConta')},
            },
        ),
    ]
