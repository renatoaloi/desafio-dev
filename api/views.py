"""CNAB Parser API Views"""
from rest_framework.views import APIView

from api.serializers import CreateCnabImportSerializer, \
    ListImportsSerializer, ListStoresSerializer
from api.models import CnabImport, Shop
from api.utils import error_response, success_response
from cnab_parser import settings


class ImportsView(APIView):
    """Imports View"""
    authentication_classes = []

    def get(self, request):
        """List imports"""
        try:
            serializer = ListImportsSerializer(
                CnabImport.objects.all().order_by(
                    '-done_date').order_by('-create_date'),
                many=True
            )
            return success_response(serializer.data)
        except Exception as err:
            return error_response(str(err))


class StoresView(APIView):
    """Stores View"""
    authentication_classes = []

    def get(self, request):
        """List stores"""
        try:
            serializer = ListStoresSerializer(
                Shop.objects.all(),
                many=True
            )
            return success_response(serializer.data)
        except Exception as err:
            return error_response(str(err))

class SchedulerView(APIView):
    """File Upload Scheduler View"""
    authentication_classes = []

    def post(self, request):
        """File upload scheduler post method"""
        try:
            CnabImport.schedule_file_process(**request.data)
            return success_response()
        except Exception as err:
            return error_response(str(err))


class CnabImportView(APIView):
    """CNAB Import View"""
    authentication_classes = []

    def post(self, request, template_id=None):
        """Create CNAB file import"""
        try:
            file = request.FILES.get('file', None)
            execution_datetime = request.POST.get('execution_datetime', None)
            if file:
                serializer = CreateCnabImportSerializer(
                    data={
                        'file': file,
                        'template_id': template_id,
                        'execution_datetime': execution_datetime
                    }
                )
                if serializer.is_valid():
                    serializer.save()
                    if not settings.TEST:
                        CnabImport.schedule_file_process(
                            recurrence=serializer.data.get('recurrence_rule'),
                            file=serializer.data.get('file'),
                            cnab_import_id=serializer.data.get('id'),
                            template_id=template_id
                        )
                    return success_response(serializer.data)
                return error_response(serializer.errors)
            return error_response('file is a required field')
        except Exception as err:
            return error_response(str(err))
