'''CNAB Parser API Models'''
import json
from datetime import datetime
import pytz
import rpyc
from dateutil.rrule import rrulestr
from django.db import models

from cnab_parser.settings import RPYC_HOST, RPYC_PORT
from backend.models import ImportTemplate


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

    owner = models.CharField(
        verbose_name='Dono da Loja',
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

    @staticmethod
    def schedule_file_process(recurrence, file, template_id):
        """Scheduler function"""
        rrules = list(rrulestr(recurrence))
        conn = rpyc.connect(RPYC_HOST, RPYC_PORT)
        for rrule in rrules:
            conn.root.add_job(
                'api:tasks.process_file',
                'date',
                args=[json.dumps({
                    'file': file,
                    'template_id': template_id
                })],
                run_date=rrule.isoformat()
            )
        conn.close()

    @staticmethod
    def convert_time_start_to_utc_date(start_time):
        """Convert rrule time start to UTC"""
        dt_local = datetime.now()
        dt_local = dt_local.replace(
            hour=start_time.hour,
            minute=start_time.minute,
            second=start_time.second
        )
        local_tz = pytz.timezone("America/Sao_Paulo")
        dt_local = local_tz.localize(dt_local)
        return dt_local.astimezone(pytz.utc)

    class Meta:
        verbose_name = 'Importação de Arquivo CNAB'
        verbose_name_plural = 'Importações de Arquivo CNAB'

    template = models.ForeignKey(
        ImportTemplate,
        verbose_name='Template de importação',
        related_name='template_fiels',
        on_delete=models.DO_NOTHING
    )

    file = models.FileField(
        verbose_name='Arquivo CNAB',
        upload_to='parser/%Y/%m/%d/',
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
        return str(self.file)
