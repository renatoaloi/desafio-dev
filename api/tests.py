"""CNAB Parser API Test file"""
from datetime import datetime

from django.urls.base import reverse
from django.test import TestCase, Client

from api.models import CnabImport, Shop
from backend.models import CnabTemplate, ImportTemplate


class CnabParserApiTest(TestCase):
    """CNAB Parser API Test class"""

    def __init__(self, methodName: str = ...):
        self.client = Client()
        super().__init__(methodName=methodName)

    def test_cnab_import(self):
        """Test CNAB import"""
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
            'file_import',
            kwargs={'template_id': import_template.id}
        )
        execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response = {'status_code': 0}
        with open('CNAB.txt', 'rb') as file:
            payload={
                'execution_datetime': execution_time,
                'file': file
            }
            response = self.client.post(url, payload)
        assert response.status_code == 200


class ShopApiTest(TestCase):
    """Shop API Test class"""

    def __init__(self, methodName: str = ...):
        self.client = Client()
        super().__init__(methodName=methodName)

    def test_list_stores(self):
        """Test list stores"""
        Shop.objects.create(name='teste')
        url = reverse('stores')
        response = self.client.get(url)
        data = response.json()
        assert response.status_code == 200
        assert len(data['data'])


class ImportApiTest(TestCase):
    """Import API Test class"""

    def __init__(self, methodName: str = ...):
        self.client = Client()
        super().__init__(methodName=methodName)

    def test_list_imports(self):
        """Test list imports"""
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
        CnabImport.objects.create(
            template=import_template
        )
        url = reverse('imports')
        response = self.client.get(url)
        data = response.json()
        assert response.status_code == 200
        assert len(data['data'])
