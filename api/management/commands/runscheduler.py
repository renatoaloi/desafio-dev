import pytz
from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from rpyc.utils.server import ThreadedServer
from rpyc import Service
from cnab_parser.settings import RPYC_HOST, RPYC_PORT

scheduler = BackgroundScheduler(timezone=pytz.UTC)


class ImportScheduler():

    @staticmethod
    def start():
        scheduler.start()

    @staticmethod
    def stop():
        scheduler.shutdown()


class SchedulerService(Service):
    def exposed_add_job(self, func, *args, **kwargs):
        return scheduler.add_job(func, *args, **kwargs)

    def exposed_remove_job(self, job_id, jobstore=None):
        try:
            scheduler.remove_job(job_id, jobstore)
        except Exception:
            pass


class Command(BaseCommand):
    help = "Runs file import scheduler."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando scheduler'))
        ImportScheduler.start()
        self.stdout.write(self.style.NOTICE('Iniciando threaded server'))
        server = ThreadedServer(
            SchedulerService,
            hostname=RPYC_HOST,
            port=RPYC_PORT,
            protocol_config={'allow_public_attrs': True}
        )
        try:
            self.stdout.write(self.style.SUCCESS('Servidor rodando...'))
            server.start()
        except (KeyboardInterrupt, SystemExit):
            pass
        finally:
            self.stdout.write(self.style.NOTICE('Parando servidor...'))
            ImportScheduler.stop()
            self.stdout.write(self.style.SUCCESS('Feito! Servidor terminado!'))