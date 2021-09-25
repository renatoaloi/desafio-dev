"""Scheduler task and Dramatiq actor functions file"""
import json
import logging
import dramatiq

logger = logging.getLogger(__name__)

@dramatiq.actor
def queue_parser(event):
    """Dramatiq actor broker"""
    print(event)
    if event:
        event_data=json.loads(event[-1])
        if event_data and 'file' in event_data:
            with open(event_data['file'], 'r', encoding='utf-8') as lines:
                for line in lines:
                    print(line)

def process_file(*args):
    """Scheduler task processor"""
    if args:
        print(args)
        logger.info('teste2')
        queue_parser.send(args)
