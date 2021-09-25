'''CNAB Parser API Models'''
from web.models import ImportTemplate
from django.db import models


class Shop(models.Model):
    """Shop model"""

    class Meta:
        verbose_name = 'Loja'

    name = models.CharField(
        verbose_name='Nome da Loja',
        null=True,
        blank=True,
        max_length=255
    )

    balance = models.DecimalField(
        verbose_name='Saldo Inicial',
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=16
    )

    def __str__(self) -> str:
        return self.name


class CnabImport(models.Model):
    '''CNAB Import model'''

    class Meta:
        verbose_name = 'Importação de Arquivo CNAB'
        verbose_name_plural = 'Importações de Arquivo CNAB'

    template = models.ForeignKey(
        ImportTemplate,
        verbose_name='Template de importação',
        related_name='template_fiels',
        on_delete=models.DO_NOTHING
    )

    file = models.CharField(
        verbose_name='Caminho do Arquivo',
        max_length=1024,
        null=True,
        blank=True
    )

    recurrence_rule = models.CharField(
        verbose_name='Regra de Recorrência',
        max_length=255,
        null=True,
        blank=True
    )

    done = models.BooleanField(
        verbose_name='Feito',
        default=False
    )

    create_date = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True
    )

    done_date = models.DateTimeField(
        verbose_name='Data de Feito',
        null=True,
        blank=True
    )

    rows_imported = models.IntegerField(
        verbose_name='Linhas Importadas',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.file


class ShopImport(models.Model):
    """Shop import model"""

    class Meta:
        verbose_name = 'Importações da Loja'
        verbose_name_plural = 'Importações das Lojas'

    shop = models.ForeignKey(
        Shop,
        related_name='shops',
        on_delete=models.DO_NOTHING,
        verbose_name='Loja'
    )

    cnab_import = models.ForeignKey(
        CnabImport,
        related_name='imports',
        on_delete=models.DO_NOTHING,
        verbose_name='Importação CNAB'
    )

    def __str__(self) -> str:
        return f'{self.shop.name} - {self.cnab_import.file}'
