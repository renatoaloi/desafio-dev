"""CNAB Parser API Test file"""
from datetime import datetime

from django.urls.base import reverse
from django.test import TestCase, Client

from api.models import Shop
from web.models import CnabTemplate, ImportTemplate


class CnabParserApiTest(TestCase):
    """CNAB Parser API Test class"""

    def __init__(self, methodName: str = ...):
        self.client = Client()
        super().__init__(methodName=methodName)

    def test_cnab_import(self):
        """Test CNAB import"""
        shop = Shop.objects.create(
            name='Loja teste',
            balance=0.0
        )
        cnab_template = CnabTemplate.objects.create(
            description='Campo1',
            start=1,
            end=1,
            size=1,
            commentary='primeiro campo'
        )
        import_template = ImportTemplate.objects.create(
            description='ImportTemplate1'
        )
        import_template.template.add(cnab_template)
        import_template.save()
        url = reverse(
            'shop_import',
            kwargs={
                'shop_id': shop.id
            }
        )
        execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response = {'status_code': 0}
        with open('CNAB.txt', 'rb') as file:
            payload={
                'template_id': import_template.id,
                'execution_datetime': execution_time,
                'file': file
            }
            response = self.client.post(url, payload)
        assert response.status_code == 200
