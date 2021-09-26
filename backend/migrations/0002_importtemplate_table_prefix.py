# Generated by Django 3.2.7 on 2021-09-26 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='importtemplate',
            name='table_prefix',
            field=models.CharField(blank=True, help_text='\n            Apelido a ser usado para nomear a tabela de \n            forma única para cada template de importação\n        ', max_length=255, null=True, verbose_name='Prefixo do nome da tabela'),
        ),
    ]