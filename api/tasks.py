"""Scheduler task and Dramatiq actor functions file"""
import json
import logging
import pathlib
import dramatiq
from django.utils import timezone
from api import db
from api.models import CnabImport, Shop
from backend.models import ImportTemplate, TransactionTypeTemplate

logger = logging.getLogger(__name__)

def save_done_status(cnab_import_id, len_import_data):
    """Save status done to CNAB import"""
    cnab_import = CnabImport.objects.filter(id=cnab_import_id).first()
    if cnab_import:
        cnab_import.done = True
        cnab_import.done_date = timezone.now()
        cnab_import.rows_imported = len_import_data
        cnab_import.save()

def post_process(table_name, hash_id):
    """Import post process"""
    sql = f"""
        SELECT * FROM {table_name} WHERE hash_id='{hash_id}'
    """
    results = db.custom_sql_all(sql)
    print(results)
    for result in results:
        value = result[4]
        tr_type = TransactionTypeTemplate.objects.filter(
            id=result[2]
        ).first()
        if tr_type:
            if tr_type.signal == 'minus':
                value *= -1
            shop = Shop.objects.filter(name=result[9]).first()
            if not shop:
                shop = Shop.objects.create(
                    name=result[9],
                    owner=result[8],
                    balance=value
                )
            else:
                shop.balance += value
                shop.save()


@dramatiq.actor
def queue_parser(event):
    """Dramatiq actor broker"""
    if event:
        event_data=json.loads(event[-1])
        if event_data and 'file' in event_data \
                 and 'template_id' in event_data \
                 and 'cnab_import_id' in event_data:
            template_id = event_data['template_id']
            cnab_import_id = event_data['cnab_import_id']
            import_template = ImportTemplate.objects.filter(id=template_id).first()
            if import_template:
                table_name = f"api_{import_template.table_prefix}"
                fields_with_type, fields = db.fill_fields(template_id)
                db.create_table_if_not_exists(table_name, fields_with_type)
                run_path = str(pathlib.Path(__file__).parent.resolve()).replace("\\", "/")
                file_path = f"{run_path}/..{event_data['file']}"
                import_data = db.do_import_data(file_path, template_id)
                hash_id = hash(f'{table_name}_{template_id}_{cnab_import_id}')
                db.send_it_to_database(import_data, table_name, fields, hash_id)
                save_done_status(cnab_import_id, len(import_data))
                # TODO: find a way to parametrize post processing
                post_process(table_name, hash_id)

def process_file(*args):
    """Scheduler task processor"""
    if args:
        logger.info(args)
        print(args)
        queue_parser.send(args)
