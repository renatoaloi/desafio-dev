"""Scheduler task and Dramatiq actor functions file"""
import json
import logging
import pathlib
import dramatiq
from api import db
from backend.models import ImportTemplate

logger = logging.getLogger(__name__)

@dramatiq.actor
def queue_parser(event):
    """Dramatiq actor broker"""
    if event:
        event_data=json.loads(event[-1])
        if event_data and 'file' in event_data \
                 and 'template_id' in event_data:
            template_id = event_data['template_id']
            import_template = ImportTemplate.objects.filter(id=template_id).first()
            if import_template:
                table_name = f"api_{import_template.table_prefix}"
                fields_with_type, fields = db.fill_fields(template_id)
                db.create_table_if_not_exists(table_name, fields_with_type)
                run_path = str(pathlib.Path(__file__).parent.resolve()).replace("\\", "/")
                file_path = f"{run_path}/..{event_data['file']}"
                import_data = db.do_import_data(file_path, template_id)
                db.send_it_to_database(import_data, table_name, fields)

def process_file(*args):
    """Scheduler task processor"""
    if args:
        logger.info(args)
        queue_parser.send(args)
