# Generated by Django 2.2.12 on 2020-10-12 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='dataCriacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]