"""CNAB Parser API Views"""
from rest_framework.views import APIView

from api.serializers import CreateCnabImportSerializer
from api.models import CnabImport, Shop
from api.utils import error_response, return_not_found, success_response


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

    def post(self, request, shop_id=None):
        """Create CNAB file import"""
        try:
            shop = Shop.objects.filter(id=shop_id).first()
            if shop:
                file = request.FILES.get('file', None)
                template_id = request.POST.get('template_id', None)
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
                        CnabImport.schedule_file_process(
                            recurrence=serializer.data.get('recurrence_rule'),
                            file=serializer.data.get('file')
                        )
                        return success_response(serializer.data)
                    return error_response(serializer.errors)
                return error_response('file is a required field')
            return return_not_found()
        except Exception as err:
            return error_response(str(err))
