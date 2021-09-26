"""Scheduler task and Dramatiq actor functions file"""
import json
import logging
import pathlib
import dramatiq

logger = logging.getLogger(__name__)

@dramatiq.actor
def queue_parser(event):
    """Dramatiq actor broker"""
    if event:
        event_data=json.loads(event[-1])
        if event_data and 'file' in event_data:
            run_path = str(pathlib.Path(__file__).parent.resolve()).replace("\\", "/")
            file_path = f"{run_path}/..{event_data['file']}"
            with open(file_path, 'r', encoding='utf-8') as lines:
                for line in lines:
                    print(line)

def process_file(*args):
    """Scheduler task processor"""
    if args:
        logger.info(args)
        queue_parser.send(args)
