from django.db import models

class CnabTemplate(models.Model):

    class Meta:
        verbose_name = "Template de CNAB"

    description = models.CharField(
        verbose_name="Descrição do campo",
        max_length=255,
        null=True,
        blank=True
    )
    start = models.IntegerField(
        verbose_name="Início",
        null=True,
        blank=True
    )
    end = models.IntegerField(
        verbose_name="Fim",
        null=True,
        blank=True
    )
    size = models.IntegerField(
        verbose_name="Tamanho",
        null=True,
        blank=True
    )
    commentary = models.TextField(
        verbose_name="Comentário",
        null=True,
        blank=True
    )


class TransactionTypeTemplate(models.Model):

    class Meta:
        verbose_name = "Template de Tipo de Transação"
    
    description = models.CharField(
        verbose_name="Descrição",
        max_length=255,
        null=True,
        blank=True
    )

    OPERATIONS = [
        ('in', 'Entrada'),
        ('out', 'Saída'),
    ]

    operation = models.CharField(
        max_length=3,
        choices=OPERATIONS
    )

    SIGNALS = [
        ('plus', '+'),
        ('minus', '-'),
    ]

    signal = models.CharField(
        max_length=5,
        choices=SIGNALS
    )