"""CNAB Parser API Views"""
import json
import rpyc

from dateutil.rrule import rrulestr
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cnab_parser.settings import RPYC_HOST, RPYC_PORT


class SchedulerView(APIView):
    """File Upload Scheduler View"""
    authentication_classes = []

    @staticmethod
    def schedule_file_process(recurrence, file):
        """Scheduler function"""
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
        """File upload scheduler post method"""
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
