import os
import rpyc
import json

from dateutil.rrule import rrulestr
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cnab_parser.settings import RPYC_HOST, RPYC_PORT


class SchedulerView(APIView):
    authentication_classes = []

    @staticmethod
    def schedule_file_process(recurrence, file):
        rrules = list(rrulestr(recurrence))
        conn = rpyc.connect(RPYC_HOST, RPYC_PORT)
        for rrule in rrules:
            conn.root.add_job(
                'api:tasks.process_file',
                'date',
                args=[json.dumps({
                    'file': file
                })],
                run_date=rrule.isoformat()
            )
        conn.close()

    def post(self, request):
        try:
            SchedulerView.schedule_file_process(**request.data)
            return Response({'ok': True, 'data': {}})
        except Exception as err:
            return Response(
                {
                    'ok': False,
                    'error': str(err)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
