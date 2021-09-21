from api.models import CnabTemplate, TransactionTypeTemplate
from django.test import TestCase
from django.db import IntegrityError

class TestTemplateModel(TestCase):

    def test_create_cnab_template(self):
        CnabTemplate.objects.create(
            description='tipo',
            start=1,
            end=1,
            size=1,
            commentary='Tipo da transação'
        )
        self.assertEqual(CnabTemplate.objects.count(), 1)

    def test_create_transaction_type_template(self):
        TransactionTypeTemplate.objects.create(
            description='Débito',
            operation='in',
            signal='plus'
        )
        self.assertEqual(TransactionTypeTemplate.objects.count(), 1)
