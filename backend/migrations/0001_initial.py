# Generated by Django 3.2.7 on 2021-09-27 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CnabTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, help_text='Descrição do campo CNAB', max_length=255, null=True, verbose_name='Descrição do campo')),
                ('field_name', models.CharField(blank=True, help_text='Nome do campo para criação da tabela', max_length=255, null=True, verbose_name='Nome do campo')),
                ('start', models.IntegerField(blank=True, help_text='Inicio do campo CNAB', null=True, verbose_name='Início')),
                ('end', models.IntegerField(blank=True, help_text='Fim do campo CNAB', null=True, verbose_name='Fim')),
                ('size', models.IntegerField(blank=True, help_text='Tamanho do campo CNAB', null=True, verbose_name='Tamanho')),
                ('commentary', models.TextField(blank=True, help_text='Comentário do campo CNAB', null=True, verbose_name='Comentário')),
                ('data_type', models.CharField(blank=True, choices=[('int', 'Número inteiro'), ('varchar', 'String de texto'), ('decimal', 'Número decimal'), ('date', 'Data'), ('timestamp', 'Data e hora')], help_text='Formatos permitidos: (int, varchar, decimal, date e timestamp)', max_length=255, null=True, verbose_name='Tipo de dados do campo')),
                ('type_format', models.CharField(blank=True, help_text='Exemplo: %Y-%m-%d para formatar uma data', max_length=255, null=True, verbose_name='Formatação do campo')),
            ],
            options={
                'verbose_name': 'Template de Campos de CNAB',
            },
        ),
        migrations.CreateModel(
            name='ImportCnabTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, help_text='Ordem dos campos do formato CNAB', null=True, verbose_name='Ordem do campo CNAB')),
                ('cnab_template', models.ForeignKey(help_text='Template de campos do formato CNAB', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.cnabtemplate', verbose_name='Template CNAB')),
            ],
            options={
                'verbose_name': 'Import CNAB Template',
            },
        ),
        migrations.CreateModel(
            name='TransactionTypeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, help_text='Descrição do tipo de transação', max_length=255, null=True, verbose_name='Descrição')),
                ('operation', models.CharField(choices=[('in', 'Entrada'), ('out', 'Saída')], help_text='Natureza da operação', max_length=3, verbose_name='Natureza')),
                ('signal', models.CharField(choices=[('plus', '+'), ('minus', '-')], help_text='Sinal da operação', max_length=5, verbose_name='Sinal')),
            ],
            options={
                'verbose_name': 'Template de Tipo de Transação',
                'verbose_name_plural': 'Template de Tipo de Transações',
            },
        ),
        migrations.CreateModel(
            name='ImportTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, help_text='Descrição do template de importação', max_length=255, null=True, verbose_name='Descrição')),
                ('table_prefix', models.CharField(blank=True, help_text='\n            Apelido a ser usado para nomear a tabela de \n            forma única para cada template de importação\n        ', max_length=255, null=True, verbose_name='Prefixo do nome da tabela')),
                ('template', models.ManyToManyField(help_text='Template de campos do formato CNAB', related_name='import_templates', through='backend.ImportCnabTemplate', to='backend.CnabTemplate')),
            ],
            options={
                'verbose_name': 'Template de Importação',
                'verbose_name_plural': 'Template de Importações',
            },
        ),
        migrations.AddField(
            model_name='importcnabtemplate',
            name='import_template',
            field=models.ForeignKey(help_text='Template importação que organiza os campos do formato CNAB', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.importtemplate', verbose_name='Template de Importação'),
        ),
    ]
