# Generated by Django 3.2.7 on 2021-09-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CnabTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição do campo')),
                ('start', models.IntegerField(blank=True, null=True, verbose_name='Início')),
                ('end', models.IntegerField(blank=True, null=True, verbose_name='Fim')),
                ('size', models.IntegerField(blank=True, null=True, verbose_name='Tamanho')),
                ('commentary', models.TextField(blank=True, null=True, verbose_name='Comentário')),
            ],
            options={
                'verbose_name': 'Template de CNAB',
            },
        ),
        migrations.CreateModel(
            name='TransactionTypeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição')),
                ('operation', models.CharField(choices=[('in', 'Entrada'), ('out', 'Saída')], max_length=3)),
                ('signal', models.CharField(choices=[('plus', '+'), ('minus', '-')], max_length=5)),
            ],
            options={
                'verbose_name': 'Template de Tipo de Transação',
            },
        ),
    ]
