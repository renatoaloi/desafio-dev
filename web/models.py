"""API Model"""
from django.db import models


class CnabTemplate(models.Model):
    """Model CnabTemplate"""

    class Meta:
        """Meta CnabTemplate"""
        verbose_name = 'Template de Campos de CNAB'

    def __str__(self):
        return self.description


    description = models.CharField(
        verbose_name='Descrição do campo',
        help_text='Descrição do campo CNAB',
        max_length=255,
        null=True,
        blank=True
    )
    start = models.IntegerField(
        verbose_name='Início',
        help_text='Inicio do campo CNAB',
        null=True,
        blank=True
    )
    end = models.IntegerField(
        verbose_name='Fim',
        help_text='Fim do campo CNAB',
        null=True,
        blank=True
    )
    size = models.IntegerField(
        verbose_name='Tamanho',
        help_text='Tamanho do campo CNAB',
        null=True,
        blank=True
    )
    commentary = models.TextField(
        verbose_name='Comentário',
        help_text='Comentário do campo CNAB',
        null=True,
        blank=True
    )


class TransactionTypeTemplate(models.Model):
    """Model TransactionTypeTemplate"""

    class Meta:
        """Meta TransactionTypeTemplate"""
        verbose_name = 'Template de Tipo de Transação'
        verbose_name_plural = 'Template de Tipo de Transações'

    def __str__(self):
        return f'{self.description} - {self.operation}'

    description = models.CharField(
        verbose_name='Descrição',
        help_text='Descrição do tipo de transação',
        max_length=255,
        null=True,
        blank=True
    )

    OPERATIONS = [
        ('in', 'Entrada'),
        ('out', 'Saída'),
    ]

    operation = models.CharField(
        verbose_name='Natureza',
        help_text='Natureza da operação',
        max_length=3,
        choices=OPERATIONS
    )

    SIGNALS = [
        ('plus', '+'),
        ('minus', '-'),
    ]

    signal = models.CharField(
        verbose_name='Sinal',
        help_text='Sinal da operação',
        max_length=5,
        choices=SIGNALS
    )


class ImportTemplate(models.Model):
    """Model ImportTemplate"""

    class Meta:
        """Meta ImportTemplate"""
        verbose_name = 'Template de Importação'
        verbose_name_plural = 'Template de Importações'

    def __str__(self):
        return self.description

    description = models.CharField(
        verbose_name='Descrição',
        help_text='Descrição do template de importação',
        max_length=255,
        null=True,
        blank=True
    )

    template = models.ManyToManyField(
        CnabTemplate,
        through='ImportCnabTemplate',
        related_name='import_templates',
        help_text='Template de campos do formato CNAB'
    )


class ImportCnabTemplate(models.Model):
    """Model ImportCnabTemplate"""

    class Meta:
        """Meta ImportCnabTemplate"""
        verbose_name = 'Import CNAB Template'

    def __str__(self):
        return f'{self.cnab_template.description} - {self.order}'

    cnab_template = models.ForeignKey(
        CnabTemplate,
        on_delete=models.DO_NOTHING,
        verbose_name='Template CNAB',
        help_text='Template de campos do formato CNAB'
    )

    import_template = models.ForeignKey(
        ImportTemplate,
        on_delete=models.DO_NOTHING,
        verbose_name='Template de Importação',
        help_text='Template importação que organiza os campos do formato CNAB'
    )

    order = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Ordem do campo CNAB',
        help_text='Ordem dos campos do formato CNAB'
    )

